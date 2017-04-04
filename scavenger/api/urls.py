from rest_framework import routers

from .views import BuildingViewSet, RoomViewSet, GroupViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register(prefix='buildings', viewset=BuildingViewSet)
router.register(prefix='rooms', viewset=RoomViewSet)
router.register(prefix='groups', viewset=GroupViewSet)
router.register(prefix='people', viewset=PersonViewSet)
