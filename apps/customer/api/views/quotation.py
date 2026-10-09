from apps.core.api_response import ApiResponse
from apps.core.views.base_viewset import BaseViewSet

from apps.customer.services import CustomerQuotationService

from ..serializers import CustomerQuotationListSerializer
from rest_framework.decorators import action

class CustomerQuotationViewSet(BaseViewSet):

    def list(self, request):

        request_id = self.kwargs["request_id"]

        quotations = CustomerQuotationService.list(
            request_id=request_id,
            customer=request.user,
        )

        serializer = CustomerQuotationListSerializer(
            quotations,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data
        )
    @action(
        detail=True,
        methods=["post"],
    )
    def accept(
        self,
        request,
        pk=None,
    ):

        allocation = CustomerQuotationService.accept(
            quotation_id=pk,
            customer=request.user,
        )

        return ApiResponse.success(
            message="Quotation accepted successfully.",
            data={
                "allocation_id": allocation.id,
            },
        )