from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    CustomerQuotationViewSet,
    CustomerRequestViewSet,
    PublicRequestViewSet,
)

router = DefaultRouter()

router.register(
    r"requests",
    CustomerRequestViewSet,
    basename="customer-requests",
)

router.register(
    r"quotations",
    CustomerQuotationViewSet,
    basename="customer-quotations",
)

urlpatterns = router.urls + [

    path(
        "public/instant-request/",
        PublicRequestViewSet.as_view(
            {
                "post": "create",
            }
        ),
        name="public-instant-request",
    ),

    path(
        "requests/<int:request_id>/quotations/",
        CustomerQuotationViewSet.as_view(
            {
                "get": "list",
            }
        ),
        name="customer-request-quotations",
    ),
    path(
        "public/track-request/",
        PublicRequestViewSet.as_view({
            "post": "track_request",   # if you created @action(detail=False)
        }),
        name="public-track-request",
    ),
]