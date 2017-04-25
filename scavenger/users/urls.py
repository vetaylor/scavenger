from rest_framework import routers

from .views import UserViewSet

users_router = routers.DefaultRouter()
users_router.register(prefix='users', viewset=UserViewSet)
