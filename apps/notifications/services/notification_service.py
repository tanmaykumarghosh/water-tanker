from django.db import transaction
from django.utils import timezone

from apps.core.constants import ReferenceType

from apps.notifications.models import Notification
from apps.requests.models import RequestEvent
from apps.requests.enums import (
    NotificationStatus,
    RequestEventType,
)


class NotificationService:

    @staticmethod
    @transaction.atomic
    def notify(
        *,
        recipient,
        service_request,
        title,
        message,
        notification_type,
    ):
        """
        Create a notification for a matched recipient.
        """

        notification = Notification.objects.create(
            user=recipient.recipient_user,
            title=title,
            message=message,
            notification_type=notification_type,
            reference_type=ReferenceType.SERVICE_REQUEST,
            reference_id=service_request.id,
        )

        recipient.sent_at = timezone.now()
        recipient.save(update_fields=["sent_at"])

        RequestEvent.objects.create(
            service_request=service_request,
            user=recipient.recipient_user,
            event_type=RequestEventType.NOTIFICATION_SENT,
            title="Notification Sent",
            description=f"Notification sent to {recipient.recipient_user.phone}.",
        )

        return notification

    @staticmethod
    def mark_as_read(notification):

        notification.notification_status = NotificationStatus.READ
        notification.read_at = timezone.now()

        notification.save(
            update_fields=[
                "notification_status",
                "read_at",
            ]
        )

        return notification

    @staticmethod
    def send_whatsapp(*args, **kwargs):
        """
        Future implementation.
        """
        pass

    @staticmethod
    def send_sms(*args, **kwargs):
        """
        Future implementation.
        """
        pass

    @staticmethod
    def send_email(*args, **kwargs):
        """
        Future implementation.
        """
        pass

    @staticmethod
    def send_push(*args, **kwargs):
        """
        Future implementation.
        """
        pass