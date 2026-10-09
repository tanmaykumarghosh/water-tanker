from django.shortcuts import get_object_or_404

from apps.profiles.models import (
    DriverProfile,
    Tanker,
)


class DriverTankerService:

    @staticmethod
    def my_tankers(user):

        driver = get_object_or_404(
            DriverProfile,
            user=user,
        )

        return (
            Tanker.objects
            .select_related(
                "capacity",
            )
            .filter(
                driver=driver,
                is_active=True,
            )
            .order_by(
                "plate_number",
            )
        )