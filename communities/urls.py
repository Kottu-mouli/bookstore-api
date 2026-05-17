from rest_framework.routers import DefaultRouter
from .views import CommunityViewSet, EventViewSet

router = DefaultRouter()
router.register('communities', CommunityViewSet)
router.register('events', EventViewSet)

urlpatterns = router.urls