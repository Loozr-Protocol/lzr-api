from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin-super-site/', admin.site.urls),

    path('api/waitlist/', include('waitlist.urls'))
]
