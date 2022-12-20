from .models import User
from rest_framework import viewsets
from .serializers import GetUserSerializer
from rest_framework import mixins

class UserViewSet(
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

class UserViewSetOne(
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = GetUserSerializer
    queryset = User.objects.all()
    lookup_field = "username"

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)