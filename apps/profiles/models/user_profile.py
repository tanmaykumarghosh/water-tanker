from django.contrib.gis.db import models

from apps.accounts.models import User
from apps.common.models import Country, Province, District


class UserProfile(models.Model):

    class Gender(models.TextChoices):
        MALE = "MALE", "Male"
        FEMALE = "FEMALE", "Female"
        OTHER = "OTHER", "Other"

    id = models.BigAutoField(primary_key=True)

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="user_profile",
    )

    gender = models.CharField(
        max_length=20,
        choices=Gender.choices,
        blank=True,
        null=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    country = models.ForeignKey(
        Country,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="country_id",
    )

    province = models.ForeignKey(
        Province,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="province_id",
    )

    district = models.ForeignKey(
        District,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="district_id",
    )

    address = models.TextField(
        blank=True,
        null=True,
    )

    location = models.PointField(
        geography=True,
        srid=4326,
        blank=True,
        null=True,
    )

    profile_photo = models.TextField(
        blank=True,
        null=True,
    )

    preferred_language = models.CharField(
        max_length=10,
        default="en",
    )

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "user_profiles"
        managed = False

    def __str__(self):
        return self.user.full_name

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