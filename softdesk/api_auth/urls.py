from django.urls import path, include
from rest_framework import routers
from api_auth.views import UserViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'user', UserViewSet)

urlpatterns = [
    path("", include(router.urls)),  
]