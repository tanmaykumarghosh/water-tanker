from rest_framework.permissions import AllowAny

from apps.common.api.serializers import CountrySerializer
from apps.common.services import LocationService
from apps.core.api_response import ApiResponse
from apps.core.views.base_viewset import BaseViewSet


class CountryViewSet(BaseViewSet):

    permission_classes = [AllowAny]

    serializer_class = CountrySerializer

    def list(self, request):

        queryset = LocationService.countries()

        serializer = self.get_serializer(
            queryset,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data,
        )