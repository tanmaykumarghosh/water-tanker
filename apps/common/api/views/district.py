from rest_framework.permissions import AllowAny

from apps.common.api.serializers import DistrictSerializer
from apps.common.services import LocationService
from apps.core.api_response import ApiResponse
from apps.core.views.base_viewset import BaseViewSet


class DistrictViewSet(BaseViewSet):

    permission_classes = [AllowAny]

    serializer_class = DistrictSerializer

    def list(self, request):

        province_id = request.query_params.get(
            "province_id"
        )

        queryset = LocationService.districts(
            province_id=province_id,
        )

        serializer = self.get_serializer(
            queryset,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data,
        )