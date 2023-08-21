from django.urls import path, include
from rest_framework import routers
from api_softdesk.views import ProjectViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'project', ProjectViewSet)

urlpatterns = [
    path("", include(router.urls)),
    
]