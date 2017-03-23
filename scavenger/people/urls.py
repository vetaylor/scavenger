from rest_framework import routers
from .views import GroupViewSet, PersonViewSet

router = routers.DefaultRouter()
router.register(prefix='groups', viewset=GroupViewSet)
router.register(prefix='people', viewset=PersonViewSet)

urlpatterns = router.urls
