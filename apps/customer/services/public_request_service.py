from django.contrib.gis.geos import Point
from django.db import transaction

from apps.accounts.models import User
from apps.profiles.models import UserProfile
from apps.requests.services import RequestService


class PublicRequestService:

    @classmethod
    @transaction.atomic
    def create(cls, *, data, request=None):
        """
        Create a public instant request.

        Workflow:
        1. Find or create customer.
        2. Update customer profile.
        3. Create service request.
        """

        phone = data.pop("phone")
        first_name = data.pop("first_name")

        # latitude = data.pop("latitude")
        # longitude = data.pop("longitude")

        # delivery_location = Point(
        #     longitude,
        #     latitude,
        #     srid=4326,
        # )
        delivery_location = data["delivery_location"]

        user = cls.get_or_create_customer(
            phone=phone,
            first_name=first_name,
        )

        cls.update_profile(
            user=user,
            data=data,
            delivery_location=delivery_location,
        )

        data["delivery_location"] = delivery_location

        return RequestService.create(
            requester=user,
            data=data,
            request=request,
        )

    @classmethod
    def get_or_create_customer(
        cls,
        *,
        phone,
        first_name,
    ):
        """
        Find an existing customer by phone or create a new one.
        """

        user = User.objects.filter(
            phone=phone,
        ).first()

        if user:
            if not user.first_name:
                user.first_name = first_name
                user.save(update_fields=["first_name"])

            return user

        user = User.objects.create_user(
            phone=phone,
            first_name=first_name,
            role=User.Role.CUSTOMER,
        )

        user.set_unusable_password()

        user.save(
            update_fields=["password"],
        )

        return user

    @classmethod
    def update_profile(
        cls,
        *,
        user,
        data,
        delivery_location,
    ):
        """
        Create or update the customer's profile.
        """

        profile, _ = UserProfile.objects.get_or_create(
            user=user,
        )

        profile.country_id = data["country_id"]
        profile.province_id = data["province_id"]
        profile.district_id = data.get("district_id")
        profile.address = data["delivery_address"]
        profile.location = delivery_location

        profile.save()

        return profile
    