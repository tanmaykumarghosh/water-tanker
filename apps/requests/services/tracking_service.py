from django.db import transaction

from apps.requests.models import (
    RequestEvent,
    RequestStatusHistory,
    DeliveryTracking,
    RequestAllocation
)
from apps.requests.enums import (
    TrackingStatus,
    AllocationStatus,
)

from django.utils import timezone

class TrackingService:

    @staticmethod
    @transaction.atomic
    def add_status(
        *,
        service_request,
        status,
        changed_by=None,
        remarks=None,
    ):
        """
        Update the current request status and create history.
        """

        service_request.status = status
        service_request.save(update_fields=["status", "updated_at"])

        return RequestStatusHistory.objects.create(
            service_request=service_request,
            status=status,
            changed_by_user=changed_by,
            remarks=remarks,
        )

    @staticmethod
    def add_event(
        *,
        service_request,
        event_type,
        user=None,
        allocation=None,
        title=None,
        description=None,
        event_data=None,
        ip_address=None,
    ):
        """
        Add a request event.
        """

        return RequestEvent.objects.create(
            service_request=service_request,
            allocation=allocation,
            user=user,
            event_type=event_type,
            title=title,
            description=description,
            event_data=event_data,
            ip_address=ip_address,
        )

    @staticmethod
    def add_status_and_event(
        *,
        service_request,
        status,
        event_type,
        changed_by=None,
        allocation=None,
        remarks=None,
        title=None,
        description=None,
        event_data=None,
        ip_address=None,
    ):
        """
        Change status and create an event in one transaction.
        """

        with transaction.atomic():

            history = TrackingService.add_status(
                service_request=service_request,
                status=status,
                changed_by=changed_by,
                remarks=remarks,
            )

            event = TrackingService.add_event(
                service_request=service_request,
                event_type=event_type,
                user=changed_by,
                allocation=allocation,
                title=title,
                description=description,
                event_data=event_data,
                ip_address=ip_address,
            )

            return history, event
    
    # @staticmethod
    # def update_location(
    #     allocation: RequestAllocation,
    #     latitude,
    #     longitude,
    #     tracking_status,
    #     accuracy=None,
    #     speed=None,
    #     heading=None,
    # ):
    #     """
    #     Save driver's current GPS location.
    #     """

    #     tracking = DeliveryTracking.objects.create(
    #         allocation=allocation,
    #         latitude=latitude,
    #         longitude=longitude,
    #         accuracy=accuracy,
    #         speed=speed,
    #         heading=heading,
    #         tracking_status=tracking_status,
    #         tracked_at=timezone.now(),
    #     )

    #     return tracking
    
    @staticmethod
    def update_location(
        *,
        allocation,
        latitude,
        longitude,
        tracking_status,
        accuracy=None,
        speed=None,
        heading=None,
    ):

        return DeliveryTracking.objects.create(
            allocation=allocation,
            latitude=latitude,
            longitude=longitude,
            accuracy=accuracy,
            speed=speed,
            heading=heading,
            tracking_status=tracking_status,
            tracked_at=timezone.now(),
        )
    


    @staticmethod
    def latest_location(allocation: RequestAllocation):
        """
        Return the latest location of a driver.
        """

        return (
            DeliveryTracking.objects.filter(
                allocation=allocation
            )
            .order_by("-tracked_at")
            .first()
        )

    @staticmethod
    def mark_on_the_way(allocation: RequestAllocation):

        allocation.allocation_status = AllocationStatus.ON_THE_WAY
        allocation.departed_at = timezone.now()

        allocation.save(
            update_fields=[
                "allocation_status",
                "departed_at",
                "updated_at",
            ]
        )

        return TrackingService.update_location(
            allocation=allocation,
            latitude=0,
            longitude=0,
            tracking_status=TrackingStatus.ON_THE_WAY,
        )

    @staticmethod
    def mark_arrived(
        allocation: RequestAllocation,
        latitude,
        longitude,
    ):

        return TrackingService.update_location(
            allocation=allocation,
            latitude=latitude,
            longitude=longitude,
            tracking_status=TrackingStatus.ARRIVED,
        )

    @staticmethod
    def start_delivery(
        allocation: RequestAllocation,
        latitude,
        longitude,
    ):

        allocation.allocation_status = AllocationStatus.DELIVERY_STARTED
        allocation.delivery_started_at = timezone.now()

        allocation.save(
            update_fields=[
                "allocation_status",
                "delivery_started_at",
                "updated_at",
            ]
        )

        return TrackingService.update_location(
            allocation=allocation,
            latitude=latitude,
            longitude=longitude,
            tracking_status=TrackingStatus.DELIVERY_STARTED,
        )

    @staticmethod
    def complete_delivery(
        allocation: RequestAllocation,
        latitude,
        longitude,
    ):

        allocation.allocation_status = AllocationStatus.COMPLETED
        allocation.completed_at = timezone.now()

        allocation.save(
            update_fields=[
                "allocation_status",
                "completed_at",
                "updated_at",
            ]
        )

        return TrackingService.update_location(
            allocation=allocation,
            latitude=latitude,
            longitude=longitude,
            tracking_status=TrackingStatus.COMPLETED,
        )