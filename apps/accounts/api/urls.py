from rest_framework.routers import DefaultRouter

from django.urls import path

from .views import AuthViewSet

urlpatterns = [
    path(
        "login/",
        AuthViewSet.as_view({
            "post": "create",
        }),
        name="login",
    ),
    path(
        "me/",
        AuthViewSet.as_view({
            "get": "me",
        }),
        name="me",
    ),
]