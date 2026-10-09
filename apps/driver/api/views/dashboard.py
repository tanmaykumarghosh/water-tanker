from rest_framework.views import APIView

from apps.core.api_response import ApiResponse

from apps.driver.services.dashboard_service import (
    DriverDashboardService,
)

from ..serializers.dashboard import (
    DriverDashboardSerializer,
)


class DriverDashboardView(APIView):

    def get(self, request):

        data = DriverDashboardService.summary(
            request.user,
        )

        serializer = DriverDashboardSerializer(
            data,
        )

        return ApiResponse.success(
            data=serializer.data,
        )