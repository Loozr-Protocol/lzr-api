from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager
)

from config.models import BaseModel


class UserManager(BaseUserManager):
    def create_superuser(self, email, password, **extra_fields):
        """Creates an admin account with the given arguments when the createsuperuser
        command is run.

        Args:
            email (string): admin email
            password (string): password

        Returns:
            User object for created account
        """
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField('Username', max_length=100, db_index=True)
    phone = models.CharField(
        'Phone Number', max_length=20, db_index=True, unique=True)
    email = models.EmailField('Email Address', max_length=150, db_index=True,
                              unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_super_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'phone']

    objects = UserManager()

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self
