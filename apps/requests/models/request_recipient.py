import uuid

from django.db import models

from apps.accounts.models import User
from .service_request import ServiceRequest
from ..enums import NotificationChannel, RecipientResponse


class RequestRecipient(models.Model):

    id = models.BigAutoField(primary_key=True)

    service_request = models.ForeignKey(
        ServiceRequest,
        on_delete=models.CASCADE,
        db_column="service_request_id",
        related_name="recipients",
    )

    recipient_user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="recipient_user_id",
        related_name="request_notifications",
    )

    notification_channel = models.CharField(
        max_length=20,
        choices=NotificationChannel.choices,
    )

    distance_km = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        blank=True,
        null=True,
    )

    sent_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    delivered_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    viewed_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    responded_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    response = models.CharField(
        max_length=20,
        choices=RecipientResponse.choices,
        default=RecipientResponse.PENDING,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "request_recipients"
        managed = False
        ordering = ["-id"]
        unique_together = (
            ("service_request", "recipient_user"),
        )

    def __str__(self):
        return f"{self.service_request.request_number} -> {self.recipient_user.phone}"