from django.urls import path, include
from rest_framework import routers
from api_softdesk.views import ProjectViewSet, IssueViewSet, ContributorViewSet


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'project', ProjectViewSet)
router.register(r'issue', IssueViewSet)
router.register(r'contributor', ContributorViewSet)
urlpatterns = [
    path("", include(router.urls)),
    
]