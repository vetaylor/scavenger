from rest_framework import routers

from .views import BuildingViewSet, RoomViewSet, GroupViewSet, PersonViewSet

api_router = routers.DefaultRouter()
api_router.register(prefix='buildings', viewset=BuildingViewSet)
api_router.register(prefix='rooms', viewset=RoomViewSet)
api_router.register(prefix='groups', viewset=GroupViewSet)
api_router.register(prefix='people', viewset=PersonViewSet)
