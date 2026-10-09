from django.contrib.gis.db import models

from apps.accounts.models import User


class DriverProfile(models.Model):

    id = models.BigAutoField(primary_key=True)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="driver_profile",
    )

    national_id = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    driving_license = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    is_online = models.BooleanField(default=False)

    is_available = models.BooleanField(default=True)

    current_location = models.PointField(
        geography=True,
        srid=4326,
        blank=True,
        null=True,
    )

    last_location_update = models.DateTimeField(
        blank=True,
        null=True,
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=5.00,
    )

    total_completed_jobs = models.IntegerField(default=0)

    created_at = models.DateTimeField()

    updated_at = models.DateTimeField()

    class Meta:
        db_table = "driver_profiles"
        managed = False

    def __str__(self):
        return self.user.phone