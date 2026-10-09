from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.allocation import RequestAllocationViewSet
# from .views.quotation import QuotationViewSet
from .views.service_request import ServiceRequestViewSet

router = DefaultRouter()

router.register(
    r"service-requests",
    ServiceRequestViewSet,
    basename="service-request",
)

# router.register(
#     r"quotations",
#     QuotationViewSet,
#     basename="quotation",
# )

router.register(
    r"driver/jobs",
    RequestAllocationViewSet,
    basename="driver-job",
)

urlpatterns = [
    path("", include(router.urls)),
]