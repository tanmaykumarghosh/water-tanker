from apps.requests.enums import (
    RecipientResponse,
    AllocationStatus,
)

from apps.requests.models import (
    RequestRecipient,
    RequestAllocation,
)


class DriverDashboardService:

    @staticmethod

    def test():
        return []

    # @staticmethod
    # def summary(user):

    #     available_requests = (
    #         RequestRecipient.objects
    #         .filter(
    #             recipient_user=user,
    #             response__in=[
    #                 RecipientResponse.PENDING,
    #                 RecipientResponse.VIEWED,
    #             ],
    #         )
    #         .count()
    #     )

    #     active_jobs = (
    #         RequestAllocation.objects
    #         .filter(
    #             driver=user,
    #             allocation_status__in=[
    #                 AllocationStatus.ACCEPTED,
    #                 AllocationStatus.DEPARTED,
    #                 AllocationStatus.ARRIVED,
    #                 AllocationStatus.DELIVERY_STARTED,
    #             ],
    #         )
    #         .count()
    #     )

    #     completed_jobs = (
    #         RequestAllocation.objects
    #         .filter(
    #             driver=user,
    #             allocation_status=AllocationStatus.COMPLETED,
    #         )
    #         .count()
    #     )

    #     latest_requests = (
    #         RequestRecipient.objects
    #         .select_related(
    #             "service_request",
    #             "service_request__capacity",
    #         )
    #         .filter(
    #             recipient_user=user,
    #             response__in=[
    #                 RecipientResponse.PENDING,
    #                 RecipientResponse.VIEWED,
    #             ],
    #         )
    #         .order_by("-created_at")[:10]
    #     )

    #     return {
    #         "available_requests": available_requests,
    #         "active_jobs": active_jobs,
    #         "completed_jobs": completed_jobs,
    #         "latest_requests": latest_requests,
    #     }