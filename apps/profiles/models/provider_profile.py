from django.contrib.gis.db import models

from apps.accounts.models import User


class ProviderProfile(models.Model):

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="provider_profile",
    )

    company_name = models.CharField(
        max_length=200,
    )

    business_registration = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    tax_number = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    business_address = models.TextField(
        blank=True,
        null=True,
    )

    # PostGIS Point
    business_location = models.PointField(
        geography=True,
        srid=4326,
        blank=True,
        null=True,
    )

    rating = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        default=5.00,
    )

    total_contracts = models.IntegerField(
        default=0,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    updated_at = models.DateTimeField(
        auto_now=True,
    )

    class Meta:
        managed = False
        db_table = "provider_profiles"

    def __str__(self):
        return self.company_name
    
    @property
    def first_name(self):
        return self.user.first_name

    @property
    def middle_name(self):
        return self.user.middle_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def phone(self):
        return self.user.phone

    @property
    def email(self):
        return self.user.email