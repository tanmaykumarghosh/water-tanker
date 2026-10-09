from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.requests.api.serializers.allocation import (
    AllocationDetailSerializer,
    AllocationListSerializer,
)
from apps.requests.models import RequestAllocation
from apps.requests.services.allocation_service import AllocationService
from apps.requests.services.tracking_service import TrackingService


from apps.requests.api.serializers.delivery import (
    CompleteDeliverySerializer,
)
from apps.requests.api.serializers.otp import (
    VerifyOTPSerializer,
)
from apps.requests.services.delivery_service import DeliveryService
from apps.requests.services.otp_service import OTPService

class RequestAllocationViewSet(viewsets.ReadOnlyModelViewSet):

    queryset = (
        RequestAllocation.objects.select_related(
            "service_request",
            "driver__user",
            "tanker",
            "allocated_capacity",
        )
        .all()
    )

    lookup_field = "uuid"

    def get_serializer_class(self):

        if self.action == "retrieve":
            return AllocationDetailSerializer

        return AllocationListSerializer

    @action(detail=True, methods=["post"])
    def accept(self, request, uuid=None):

        allocation = self.get_object()

        allocation = AllocationService.accept(allocation)

        serializer = AllocationDetailSerializer(allocation)

        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def reject(self, request, uuid=None):

        allocation = self.get_object()

        allocation = AllocationService.reject(allocation)

        serializer = AllocationDetailSerializer(allocation)

        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def depart(self, request, uuid=None):

        allocation = self.get_object()

        TrackingService.mark_on_the_way(allocation)

        serializer = AllocationDetailSerializer(allocation)

        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def arrived(self, request, uuid=None):

        allocation = self.get_object()

        latitude = request.data.get("latitude")
        longitude = request.data.get("longitude")

        TrackingService.mark_arrived(
            allocation=allocation,
            latitude=latitude,
            longitude=longitude,
        )

        serializer = AllocationDetailSerializer(allocation)

        return Response(serializer.data)

    @action(detail=True, methods=["post"])
    def delivery_start(self, request, uuid=None):

        allocation = self.get_object()

        latitude = request.data.get("latitude")
        longitude = request.data.get("longitude")

        TrackingService.start_delivery(
            allocation=allocation,
            latitude=latitude,
            longitude=longitude,
        )

        serializer = AllocationDetailSerializer(allocation)

        return Response(serializer.data)
    
    @action(detail=True, methods=["post"], url_path="generate-otp")
    def generate_otp(self, request, uuid=None):

        allocation = self.get_object()

        delivery_otp = OTPService.create_otp(allocation)

        # TODO:
        # NotificationService.send_delivery_otp(
        #     phone=allocation.service_request.customer.phone,
        #     otp=delivery_otp.otp,
        # )

        return Response(
            {
                "success": True,
                "message": "OTP generated successfully.",
            },
            status=status.HTTP_200_OK,
        )
    @action(detail=True, methods=["post"], url_path="verify-otp")
    def verify_otp(self, request, uuid=None):

        allocation = self.get_object()

        serializer = VerifyOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        success, result = OTPService.verify_otp(
            allocation=allocation,
            otp=serializer.validated_data["otp"],
        )

        if not success:
            return Response(
                {
                    "success": False,
                    "message": result,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "success": True,
                "message": "OTP verified successfully.",
            },
            status=status.HTTP_200_OK,
        )
    @action(detail=True, methods=["post"], url_path="complete")
    def complete(self, request, uuid=None):

        allocation = self.get_object()

        serializer = CompleteDeliverySerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        success, result = DeliveryService.complete_delivery(
            allocation=allocation,
            uploaded_by=request.user,
            **serializer.validated_data,
        )

        if not success:
            return Response(
                {
                    "success": False,
                    "message": result,
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        return Response(
            {
                "success": True,
                "message": "Delivery completed successfully.",
            },
            status=status.HTTP_200_OK,
        )