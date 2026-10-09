from django.db import models

from apps.accounts.models import User
from ..enums import (
    NotificationType,
    NotificationStatus,
)


class Notification(models.Model):

    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        db_column="user_id",
        related_name="notifications",
    )

    title = models.CharField(
        max_length=255,
    )

    message = models.TextField()

    notification_type = models.CharField(
        max_length=30,
        choices=NotificationType.choices,
    )

    notification_status = models.CharField(
        max_length=20,
        choices=NotificationStatus.choices,
        default=NotificationStatus.UNREAD,
    )

    reference_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    reference_id = models.BigIntegerField(
        blank=True,
        null=True,
    )

    read_at = models.DateTimeField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "notifications"
        managed = False
        ordering = ["-created_at"]

    def __str__(self):
        return self.title