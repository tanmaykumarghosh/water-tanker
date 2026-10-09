from apps.core.api_response import ApiResponse
from apps.core.views.base_viewset import BaseViewSet
from rest_framework.decorators import action

from apps.driver.services import DriverRequestService

from rest_framework import status

from ..serializers import (
    DriverRequestListSerializer,
    DriverRequestDetailSerializer,
    AcceptRequestSerializer,
)
import logging

logger = logging.getLogger(__name__)
class DriverRequestViewSet(BaseViewSet):

    def list(self, request):

        logger.info("View called")

        queryset = DriverRequestService.inbox(
            request.user
        )

        serializer = DriverRequestListSerializer(
            queryset,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data
        )
    
    def retrieve(self, request, pk=None):

        recipient = DriverRequestService.get_request(
            recipient_id=pk,
            user=request.user,
        )

        serializer = DriverRequestDetailSerializer(
            recipient
        )

        return ApiResponse.success(
            data=serializer.data
        )
    
    @action(
        detail=True,
        methods=["post"],
    )
    def accept(self, request, pk=None):

        serializer = AcceptRequestSerializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        allocation = DriverRequestService.accept(
            recipient_id=pk,
            tanker_id=serializer.validated_data["tanker_id"],
            user=request.user,
        )

        return ApiResponse.success(
            message="Request accepted successfully.",
            data={
                "allocation_id": allocation.id,
                "allocation_uuid": allocation.uuid,
            },
        )
    
    @action(
        detail=True,
        methods=["post"],
    )
    def reject(self, request, pk=None):

        DriverRequestService.reject(
            recipient_id=pk,
            user=request.user,
        )

        return ApiResponse.success(
            message="Request rejected successfully.",
            status_code=status.HTTP_200_OK,
        )