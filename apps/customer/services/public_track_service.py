from django.shortcuts import get_object_or_404

from apps.accounts.models import User
from apps.requests.models import (
    ServiceRequest,
    RequestStatusHistory,
)


class PublicTrackService:

    @classmethod
    def track(cls, *, request_number, phone):

        user = get_object_or_404(
            User,
            phone=phone,
        )

        service_request = get_object_or_404(
            ServiceRequest,
            request_number=request_number,
            requester_user=user,
        )

        history = (
            RequestStatusHistory.objects
            .filter(service_request=service_request)
            .order_by("created_at")
        )

        return {
            "request": service_request,
            "history": history,
        }