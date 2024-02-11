from django.urls import path, include


urlpatterns = [
    path("snippets/", include("snippets.urls")),
]
