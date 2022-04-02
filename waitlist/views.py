from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView

from .serializers import WaitlistSerializer


class JoinWaitlist(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = WaitlistSerializer
