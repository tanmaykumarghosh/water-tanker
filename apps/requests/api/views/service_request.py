from rest_framework import status
from apps.core.views.base_viewset import BaseViewSet


from apps.core.api_response import ApiResponse
from apps.requests.models import ServiceRequest
from apps.requests.services import RequestService

from ..serializers import (
    CreateRequestSerializer,
    RequestDetailSerializer,
)


class ServiceRequestViewSet(BaseViewSet):

    queryset = ServiceRequest.objects.all()
    serializer_class = RequestDetailSerializer

    def get_serializer_class(self):

        if self.action == "create":
            return CreateRequestSerializer

        return RequestDetailSerializer

    def create(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        service_request = RequestService.create(
            requester=request.user,
            data=serializer.validated_data,
            request=request,
        )

        response_serializer = RequestDetailSerializer(service_request)

        return ApiResponse.success(
            data=response_serializer.data,
            message="Service request created successfully.",
            status_code=status.HTTP_201_CREATED,
        )

    def list(self, request):

        queryset = (
            ServiceRequest.objects
            .filter(requester_user=request.user)
            .order_by("-created_at")
        )

        serializer = RequestDetailSerializer(
            queryset,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data
        )

    def retrieve(self, request, pk=None):

        service_request = self.get_object()

        serializer = RequestDetailSerializer(service_request)

        return ApiResponse.success(
            data=serializer.data
        )