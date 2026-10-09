from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class AuthService:

    @staticmethod
    def login(phone: str, password: str):

        user = authenticate(
            phone=phone,
            password=password,
        )

        if not user:
            return None

        refresh = RefreshToken.for_user(user)

        return {
            "user": user,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }