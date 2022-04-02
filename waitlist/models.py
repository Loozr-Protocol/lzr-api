from django.db import models

from config.models import BaseModel


class Waitlist(BaseModel):
    email = models.EmailField(max_length=300, unique=True)
    category = models.CharField(max_length=200)
