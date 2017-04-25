from rest_framework import viewsets

from .models import User
from .serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """ """

    lookup_field = 'email'
    queryset = User.objects.all()
    serializer_class = UserSerializer
