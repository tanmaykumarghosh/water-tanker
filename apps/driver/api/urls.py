from rest_framework.routers import DefaultRouter
from .views.dashboard import DriverDashboardView
from .views.tanker import DriverTankerView
from .views.tracking import DriverTrackingView
from django.urls import path

from .views import (
    DriverRequestViewSet,
    DriverQuotationViewSet,
    DriverJobView,
    DriverJobStatusView,
    DriverJobHistoryView,
    DriverJobHistoryDetailView
)


router = DefaultRouter()

router.register(
    r"requests",
    DriverRequestViewSet,
    basename="driver-requests",
)

router.register(
    r"quotations",
    DriverQuotationViewSet,
    basename="driver-quotations",
)

urlpatterns = router.urls + [

    path(
        "dashboard/",
        DriverDashboardView.as_view(),
    ),

    path(
        "tankers/",
        DriverTankerView.as_view(),
    ),

    path(
        "jobs/active/",
        DriverJobView.as_view(),
    ),
    path(
        "jobs/<int:pk>/status/",
        DriverJobStatusView.as_view(),
        name="driver-job-status",
    ),
    path(
        "jobs/history/",
        DriverJobHistoryView.as_view(),
        name="driver-job-history",
    ),
    path(
        "jobs/history/<int:pk>/",
        DriverJobHistoryDetailView.as_view(),
        name="driver-job-history-detail",
    ),

     path(
        "jobs/<int:pk>/tracking/",
        DriverTrackingView.as_view(),
        name="driver-job-tracking",
    ),
]