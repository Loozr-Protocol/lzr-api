from django.urls import path

from .views import JoinWaitlist

app_name = 'waitlist'

urlpatterns = [
     path('', JoinWaitlist.as_view(), name="waitlist"),
]
