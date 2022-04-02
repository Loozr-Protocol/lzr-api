from asgiref.sync import sync_to_async
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from .models import Waitlist


class TestWaitlistAPI(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('waitlist:waitlist')

    def test_join_waitlist(self):
        data = {'category': 'Music', 'email': 'confi@gmail.com'}
        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)

    def _delete_created_waitlist(self):
        return Waitlist.objects.delete()

    def tearDown(self) -> None:
        sync_to_async(self._delete_created_waitlist, thread_sensitive=True)
