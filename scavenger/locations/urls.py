from rest_framework import routers
from .views import BuildingViewSet, RoomViewSet

router = routers.DefaultRouter()
router.register(prefix='buildings', viewset=BuildingViewSet)
router.register(prefix='rooms', viewset=RoomViewSet)

urlpatterns = router.urls
