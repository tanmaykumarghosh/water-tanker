from django.db import transaction

from apps.profiles.models import DriverProfile, Tanker
from apps.requests.models import RequestRecipient,RequestAllocation
from apps.requests.enums import (
    NotificationChannel,
    RecipientResponse,
)


class MatchingService:

    @classmethod
    @transaction.atomic
    def match(cls, service_request):
        """
        Match eligible drivers and create RequestRecipient records.
        """

        drivers = cls.find_matching_drivers(service_request)

        recipients = []

        for driver in drivers:

            recipient, created = RequestRecipient.objects.get_or_create(
                service_request=service_request,
                recipient_user=driver.user,
                defaults={
                    "notification_channel": NotificationChannel.APP,
                    "response": RecipientResponse.PENDING,
                },
            )

            recipients.append(recipient)

        return recipients
    
    @classmethod
    def find_matching_drivers(cls, service_request):

        return DriverProfile.objects.filter(
            is_online=True,
            is_available=True,
            user__is_active=True,

            tankers__is_active=True,

            tankers__status="AVAILABLE",

            tankers__capacity=service_request.capacity,

            tankers__service_type=service_request.service_type,

            user__user_profile__district=service_request.district,
        ).distinct()
    
    @classmethod
    def get_available_tanker(cls, driver, service_request):

        return (
            driver.tankers
            .filter(
                is_active=True,
                status="AVAILABLE",
                capacity=service_request.capacity,
                service_type=service_request.service_type,
            )
            .first()
        )