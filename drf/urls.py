from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

from snippets.views import SnippetViewSet, UserViewSet


router = DefaultRouter()
router.register("snippets", SnippetViewSet, basename="snippet")
router.register("users", UserViewSet, basename="user")

urlpatterns = [
    path("", include(router.urls)),
]
