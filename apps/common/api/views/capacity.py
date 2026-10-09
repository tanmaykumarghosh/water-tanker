from rest_framework.permissions import AllowAny

from apps.common.api.serializers import CapacitySerializer
from apps.common.services import CapacityService
from apps.core.api_response import ApiResponse
from apps.core.views.base_viewset import BaseViewSet


class CapacityViewSet(BaseViewSet):

    permission_classes = [AllowAny]

    serializer_class = CapacitySerializer

    def list(self, request):

        queryset = CapacityService.all()

        serializer = self.get_serializer(
            queryset,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data,
        )