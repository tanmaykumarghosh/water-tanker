from rest_framework.views import APIView

from apps.core.api_response import ApiResponse

from apps.driver.services import DriverTankerService

from ..serializers.tanker import DriverTankerSerializer


class DriverTankerView(APIView):

    def get(self, request):

        queryset = DriverTankerService.my_tankers(
            request.user,
        )

        serializer = DriverTankerSerializer(
            queryset,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data,
        )