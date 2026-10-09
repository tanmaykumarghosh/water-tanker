from django.db import transaction
from django.utils import timezone
from rest_framework.exceptions import ValidationError

from apps.profiles.models import DriverProfile, Tanker
from apps.requests.models import (
    RequestAllocation,
    RequestEvent,
)
from apps.requests.enums import (
    AllocationStatus,
    RequestStatus,
    RequestEventType,
    TrackingStatus,
)

from apps.requests.services.tracking_service import TrackingService

class DriverJobService:

    @staticmethod
    def active_job(user):

        driver = DriverProfile.objects.get(user=user)

        return (
            RequestAllocation.objects
            .select_related(
                "service_request",
                "service_request__requester_user",
                "allocated_capacity",
                "tanker",
            )
            .filter(
                driver=driver,
                allocation_status__in=[
                    AllocationStatus.ACCEPTED,
                    AllocationStatus.ARRIVED,
                    AllocationStatus.ON_THE_WAY,
                    AllocationStatus.DELIVERY_STARTED,
                ],
            )
            .order_by("-created_at")
            .first()
        )
    @staticmethod
    def history(user):

        driver = DriverProfile.objects.get(
            user=user,
        )

        return (
            RequestAllocation.objects
            .select_related(
                "service_request",
                "service_request__requester_user",
                "allocated_capacity",
                "tanker",
            )
            .filter(
                driver=driver,
                allocation_status=AllocationStatus.DELIVERED,
            )
            .order_by("-completed_at")
        )

    @staticmethod
    @transaction.atomic
    def update_status(
        *,
        allocation_id,
        status,
        latitude,
        longitude,
        accuracy,
        speed,
        heading,
        user,
    ):

        driver = DriverProfile.objects.get(user=user)

        allocation = (
            RequestAllocation.objects
            .select_for_update()
            .select_related(
                "service_request",
                "tanker",
            )
            .get(
                id=allocation_id,
                driver=driver,
            )
        )

        request = allocation.service_request

        # allocation = RequestAllocation.objects.get(
        #     id=allocation_id,
        #     driver=user,
        # )

        
        if status == AllocationStatus.ARRIVED:

            allocation.allocation_status = AllocationStatus.ARRIVED
            allocation.arrived_at = timezone.now()

            event = RequestEventType.DRIVER_ON_THE_WAY
            title = "Driver Arrived"

        

        # elif status == AllocationStatus.ON_THE_WAY:

        #     allocation.allocation_status = AllocationStatus.ON_THE_WAY
        #     allocation.departed_at = timezone.now()

        #     request.status = RequestStatus.ON_THE_WAY
        #     request.save(update_fields=["status"])

        #     event = RequestEventType.DRIVER_ON_THE_WAY
        #     title = "Driver On The Way"
        elif status == AllocationStatus.ON_THE_WAY:

            allocation.allocation_status = AllocationStatus.ON_THE_WAY
            allocation.departed_at = timezone.now()

            request.status = RequestStatus.ON_THE_WAY
            request.save(update_fields=["status"])

            event = RequestEventType.DRIVER_ON_THE_WAY
            title = "Driver On The Way"

            # allocation.save(
            #     update_fields=[
            #         "allocation_status",
            #         "departed_at",
            #         "updated_at",
            #     ]
            # )

            TrackingService.update_location(
                allocation=allocation,
                latitude=latitude,
                longitude=longitude,
                accuracy=accuracy,
                speed=speed,
                heading=heading,
                tracking_status=TrackingStatus.ON_THE_WAY,
            )


        elif status == AllocationStatus.DELIVERY_STARTED:

            allocation.allocation_status = AllocationStatus.DELIVERY_STARTED
            allocation.delivery_started_at = timezone.now()

            request.status = RequestStatus.DELIVERY_STARTED
            request.save(update_fields=["status"])

            event = RequestEventType.DELIVERY_STARTED
            title = "Delivery Started"

        elif status == AllocationStatus.DELIVERED:

            allocation.allocation_status = AllocationStatus.DELIVERED
            allocation.completed_at = timezone.now()

            request.status = RequestStatus.COMPLETED
            request.save(update_fields=["status"])

            tanker = allocation.tanker
            tanker.status = Tanker.TankerStatus.AVAILABLE
            tanker.save(update_fields=["status"])

            driver.total_completed_jobs += 1
            driver.save(update_fields=["total_completed_jobs"])

            event = RequestEventType.DELIVERY_COMPLETED
            title = "Delivery Completed"

        else:
            raise ValidationError("Invalid status.")

        allocation.save()

        RequestEvent.objects.create(
            service_request=request,
            allocation=allocation,
            user=user,
            event_type=event,
            title=title,
        )

        return allocation
    @staticmethod
    def history_detail(user, allocation_id):

        driver = DriverProfile.objects.get(
            user=user,
        )

        return (
            RequestAllocation.objects
            .select_related(
                "service_request",
                "service_request__requester_user",
                "allocated_capacity",
                "tanker",
            )
            .get(
                id=allocation_id,
                driver=driver,
            )
        )
    
    # @staticmethod
    # def update_status(
    #     *,
    #     allocation_id,
    #     status,
    #     latitude,
    #     longitude,
    #     accuracy,
    #     speed,
    #     heading,
    #     user,
    # ):

    #     allocation = RequestAllocation.objects.get(
    #         id=allocation_id,
    #         driver=user,
    #     )

    #     if status == AllocationStatus.ON_THE_WAY:

    #         allocation.allocation_status = AllocationStatus.ON_THE_WAY
    #         allocation.departed_at = timezone.now()

    #         allocation.save(
    #             update_fields=[
    #                 "allocation_status",
    #                 "departed_at",
    #                 "updated_at",
    #             ]
    #         )

    #         TrackingService.update_location(
    #             allocation=allocation,
    #             latitude=latitude,
    #             longitude=longitude,
    #             accuracy=accuracy,
    #             speed=speed,
    #             heading=heading,
    #             tracking_status=TrackingStatus.ON_THE_WAY,
    #         )

    #     return allocation