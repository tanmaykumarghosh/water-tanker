from rest_framework import status
from rest_framework.permissions import AllowAny

from apps.core.api_response import ApiResponse
from apps.core.views.base_viewset import BaseViewSet

from apps.customer.services import (
    PublicRequestService,
    PublicTrackService
)
from rest_framework.decorators import action

from ..serializers import (
    CreatePublicRequestSerializer,
    TrackRequestSerializer
)
from apps.requests.api.serializers import (
    RequestDetailSerializer,
)


class PublicRequestViewSet(BaseViewSet):
    """
    Public API for creating instant service requests.
    No authentication required.
    """

    permission_classes = [AllowAny]

    serializer_class = CreatePublicRequestSerializer

    def create(self, request):

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        service_request = PublicRequestService.create(
            data=serializer.validated_data,
            request=request,
        )

        response_serializer = RequestDetailSerializer(
            service_request,
        )

        return ApiResponse.success(
            data=response_serializer.data,
            message="Service request submitted successfully.",
            status_code=status.HTTP_201_CREATED,
        )
    
    @action(
        detail=False,
        methods=["post"],
        url_path="track-request",
    )
    def track_request(self, request):

        serializer = TrackRequestSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        result = PublicTrackService.track(
            **serializer.validated_data,
        )

        service_request = result["request"]
        history = result["history"]

        return ApiResponse.success(
            data={
                "request_number": service_request.request_number,
                "status": service_request.status,
                "history": [
                    {
                        "status": item.status,
                        "remarks": item.remarks,
                        "created_at": item.created_at,
                    }
                    for item in history
                ],
            }
        )