from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from apps.core.api_response import ApiResponse

from ..serializers.tracking import DriverTrackingSerializer
from apps.driver.services.driver_tracking_service import DriverTrackingService


class DriverTrackingView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def post(
        self,
        request,
        pk,
    ):

        serializer = DriverTrackingSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        DriverTrackingService.save_location(
            allocation_id=pk,
            user=request.user,
            **serializer.validated_data,
        )

        return ApiResponse.success(
            message="Location updated successfully.",
        )