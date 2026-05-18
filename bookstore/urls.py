from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.routers import DefaultRouter
from books.views import BookViewSet
from communities.views import CommunityViewSet, EventViewSet

router = DefaultRouter()
router.register('books', BookViewSet)
router.register('communities', CommunityViewSet)
router.register('events', EventViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view()),
    path('api/token/refresh/', TokenRefreshView.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)