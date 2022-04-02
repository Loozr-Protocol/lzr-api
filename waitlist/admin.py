from django.contrib import admin

from .models import Waitlist


class WaitlistAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'category', 'created_at',
    )


admin.site.register(Waitlist, WaitlistAdmin)
