from apps.common.models import Capacity


class CapacityService:

    @classmethod
    def all(cls):

        return (
            Capacity.objects
            .all()
            .order_by("liters")
        )