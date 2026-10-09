from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CapacityViewSet,
    CountryViewSet,
    DistrictViewSet,
    ProvinceViewSet,
)

router = DefaultRouter()

router.register(
    "countries",
    CountryViewSet,
    basename="countries",
)

router.register(
    "provinces",
    ProvinceViewSet,
    basename="provinces",
)

router.register(
    "districts",
    DistrictViewSet,
    basename="districts",
)

router.register(
    "capacities",
    CapacityViewSet,
    basename="capacities",
)

urlpatterns = [
    path("", include(router.urls)),
]