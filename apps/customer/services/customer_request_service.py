from apps.requests.models import ServiceRequest
from django.db.models import Count

class CustomerRequestService:

    @staticmethod
    def my_requests(user):

        return (
            ServiceRequest.objects
            .select_related(
                "capacity",
            )
            .filter(
                requester_user=user,
            )
            .order_by("-created_at")
        )

    @staticmethod
    def detail(user, request_id):

        return (
            ServiceRequest.objects
            .select_related(
                "capacity",
                "country",
                "province",
                "district",
            )
            .annotate(
                quotation_count=Count(
                    "quotations",
                    distinct=True,
                ),
                allocation_count=Count(
                    "allocations",
                    distinct=True,
                ),
            )
            .get(
                id=request_id,
                requester_user=user,
            )
        )