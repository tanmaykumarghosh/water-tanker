from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from apps.core.api_response import ApiResponse

from apps.driver.services.driver_job_service import DriverJobService

from ..serializers.job import (DriverActiveJobSerializer,DriverJobStatusSerializer,DriverJobHistorySerializer,DriverJobDetailSerializer)


class DriverJobView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request):

        allocation = DriverJobService.active_job(
            request.user,
        )

        if allocation is None:

            return ApiResponse.success(
                data=None,
            )

        serializer = DriverActiveJobSerializer(
            allocation,
        )

        return ApiResponse.success(
            data=serializer.data,
        )


class DriverJobStatusView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def post(
        self,
        request,
        pk,
    ):

        serializer = DriverJobStatusSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        # allocation = DriverJobService.update_status(
        #     allocation_id=pk,
        #     status=serializer.validated_data["status"],
        #     user=request.user,
        # )

        allocation = DriverJobService.update_status(
            allocation_id=pk,
            status=serializer.validated_data["status"],
            latitude=serializer.validated_data["latitude"],
            longitude=serializer.validated_data["longitude"],
            accuracy=serializer.validated_data.get("accuracy"),
            speed=serializer.validated_data.get("speed"),
            heading=serializer.validated_data.get("heading"),
            user=request.user,
        )

        return ApiResponse.success(
            message="Status updated successfully.",
            data={
                "allocation_status":
                    allocation.allocation_status,
            },
        )
    
class DriverJobHistoryView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        jobs = DriverJobService.history(
            request.user,
        )

        serializer = DriverJobHistorySerializer(
            jobs,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data,
        )
    
class DriverJobHistoryDetailView(APIView):

    permission_classes = [
        IsAuthenticated,
    ]

    def get(self, request, pk):

        allocation = DriverJobService.history_detail(
            request.user,
            pk,
        )

        serializer = DriverJobDetailSerializer(
            allocation,
        )

        return ApiResponse.success(
            data=serializer.data,
        )