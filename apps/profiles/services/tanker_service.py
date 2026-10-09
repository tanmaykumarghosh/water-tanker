from apps.profiles.models import Tanker


class TankerService:

    @staticmethod
    def available_tankers(driver):
        return Tanker.objects.filter(
            driver=driver,
            is_active=True,
            status="AVAILABLE",
        )

    @staticmethod
    def update_status(tanker, status):
        tanker.status = status
        tanker.save(update_fields=["status"])

    @staticmethod
    def capacity_match(capacity):
        return Tanker.objects.filter(
            capacity=capacity,
            is_active=True,
            status="AVAILABLE",
        )