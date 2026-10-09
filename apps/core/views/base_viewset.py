from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet


class BaseViewSet(GenericViewSet):
    """
    Base ViewSet for all APIs.
    """

    permission_classes = [IsAuthenticated]