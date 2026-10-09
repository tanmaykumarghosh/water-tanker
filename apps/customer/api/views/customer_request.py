from apps.core.api_response import ApiResponse
from apps.core.views.base_viewset import BaseViewSet

from apps.customer.services import CustomerRequestService

from ..serializers import (
    CustomerRequestListSerializer,
    CustomerRequestDetailSerializer,
)


class CustomerRequestViewSet(BaseViewSet):

    def list(self, request):

        queryset = CustomerRequestService.my_requests(
            request.user
        )

        serializer = CustomerRequestListSerializer(
            queryset,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data
        )

    def retrieve(self, request, pk=None):

        service_request = CustomerRequestService.detail(
            request.user,
            pk,
        )

        serializer = CustomerRequestDetailSerializer(
            service_request
        )

        return ApiResponse.success(
            data=serializer.data
        )