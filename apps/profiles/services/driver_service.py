from apps.profiles.models import DriverProfile


class DriverService:

    @staticmethod
    def get_driver(user):
        return DriverProfile.objects.filter(user=user).first()

    @staticmethod
    def set_online(driver):
        driver.is_online = True
        driver.save(update_fields=["is_online"])

    @staticmethod
    def set_offline(driver):
        driver.is_online = False
        driver.save(update_fields=["is_online"])

    @staticmethod
    def set_available(driver):
        driver.is_available = True
        driver.save(update_fields=["is_available"])

    @staticmethod
    def set_busy(driver):
        driver.is_available = False
        driver.save(update_fields=["is_available"])

    @staticmethod
    def update_location(driver, point):
        driver.current_location = point
        driver.save(update_fields=[
            "current_location",
            "last_location_update",
        ])