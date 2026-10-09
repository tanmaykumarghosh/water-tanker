from rest_framework.decorators import action

from apps.core.api_response import ApiResponse
from apps.core.views.base_viewset import BaseViewSet

from apps.driver.services import DriverQuotationService

from ..serializers import (
    SubmitQuotationSerializer,
    DriverQuotationListSerializer,
)


class DriverQuotationViewSet(BaseViewSet):

    # @action(
    #     detail=False,
    #     methods=["post"],
    # )
   
    
    def list(self, request):

        queryset = DriverQuotationService.my_quotations(
            request.user
        )

        serializer = DriverQuotationListSerializer(
            queryset,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data
        )

    def create(self, request):

        serializer = SubmitQuotationSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        quotation = DriverQuotationService.submit(
            request.user,
            serializer.validated_data,
        )

        return ApiResponse.success(
            message="Quotation submitted successfully.",
            data={
                "quotation_id": quotation.id,
            },
        )