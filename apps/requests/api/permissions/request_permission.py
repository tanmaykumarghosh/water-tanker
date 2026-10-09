from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdmin(BasePermission):
    """
    Allows access only to administrators.
    """

    message = "Administrator access is required."

    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated
            and user.is_superuser
        )


class IsCustomer(BasePermission):
    """
    Allows access only to customers.
    """

    message = "Customer access is required."

    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated
            and hasattr(user, "customer_profile")
        )


class IsDriver(BasePermission):
    """
    Allows access only to drivers.
    """

    message = "Driver access is required."

    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated
            and hasattr(user, "driver_profile")
        )


class IsProvider(BasePermission):
    """
    Allows access only to providers.
    """

    message = "Provider access is required."

    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated
            and hasattr(user, "provider_profile")
        )


class IsDispatcher(BasePermission):
    """
    Allows access only to dispatchers.
    """

    message = "Dispatcher access is required."

    def has_permission(self, request, view):
        user = request.user

        return (
            user.is_authenticated
            and user.is_staff
        )


class IsReadOnly(BasePermission):
    """
    Read-only permission.
    """

    def has_permission(self, request, view):
        return request.method in SAFE_METHODS