from django.shortcuts import get_object_or_404

from apps.requests.models import RequestAllocation
from apps.requests.services.tracking_service import TrackingService

from apps.profiles.models.driver_profile import DriverProfile


class DriverTrackingService:

    @staticmethod
    def save_location(
        *,
        allocation_id,
        user,
        latitude,
        longitude,
        accuracy=None,
        speed=None,
        heading=None,
    ):
        
        driver = DriverProfile.objects.get(
            user=user,
        )

        allocation = RequestAllocation.objects.get(
            id=allocation_id,
            driver=driver,
        )

        allocation = get_object_or_404(
            RequestAllocation,
            pk=allocation_id,
            driver=driver,
        )

        TrackingService.update_location(
            allocation=allocation,
            latitude=latitude,
            longitude=longitude,
            accuracy=accuracy,
            speed=speed,
            heading=heading,
            tracking_status=allocation.allocation_status,
        )

        return allocation