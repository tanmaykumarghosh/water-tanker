from rest_framework.permissions import AllowAny

from apps.common.api.serializers import ProvinceSerializer
from apps.common.services import LocationService
from apps.core.api_response import ApiResponse
from apps.core.views.base_viewset import BaseViewSet


class ProvinceViewSet(BaseViewSet):

    permission_classes = [AllowAny]

    serializer_class = ProvinceSerializer

    def list(self, request):

        country_id = request.query_params.get(
            "country_id"
        )

        queryset = LocationService.provinces(
            country_id=country_id,
        )

        serializer = self.get_serializer(
            queryset,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data,
        )