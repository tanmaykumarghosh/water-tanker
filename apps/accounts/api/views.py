from rest_framework import status
from rest_framework.permissions import (IsAuthenticated,AllowAny)
from rest_framework.decorators import action

from apps.core.api_response import ApiResponse
from apps.core.views.base_viewset import BaseViewSet

from apps.accounts.services.auth_service import AuthService
from apps.accounts.services.user_service import UserService

from .serializers import LoginSerializer


class AuthViewSet(BaseViewSet):

    permission_classes = [AllowAny]

    serializer_class = LoginSerializer

    def create(self, request):

        serializer = self.get_serializer(
            data=request.data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        result = AuthService.login(
            phone=serializer.validated_data["phone"],
            password=serializer.validated_data["password"],
        )

        if not result:

            return ApiResponse.error(
                message="Invalid phone or password.",
                status_code=status.HTTP_401_UNAUTHORIZED,
            )

        return ApiResponse.success(
            message="Login successful.",
            data={
                "access": result["access"],
                "refresh": result["refresh"],
                "user": UserService.get_profile(
                    result["user"],
                ),
            },
        )
    @action(
        detail=False,
        methods=["get"],
        permission_classes=[IsAuthenticated],
    )
    def me(self, request):

        return ApiResponse.success(
            message="Profile fetched successfully.",
            data=UserService.get_profile(
                request.user,
            ),
        )