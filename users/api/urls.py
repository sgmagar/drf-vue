from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from .viewsets import UserViewSet

router = DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    url(r'^v1/', include(router.urls)),
]
