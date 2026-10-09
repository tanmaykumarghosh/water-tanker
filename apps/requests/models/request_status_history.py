from django.db import models

from apps.accounts.models import User
from .service_request import ServiceRequest
from ..enums import RequestStatus


class RequestStatusHistory(models.Model):

    id = models.BigAutoField(primary_key=True)

    service_request = models.ForeignKey(
        ServiceRequest,
        on_delete=models.CASCADE,
        db_column="service_request_id",
        related_name="status_history",
    )

    status = models.CharField(
        max_length=30,
        choices=RequestStatus.choices,
    )

    changed_by_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="changed_by_user_id",
        related_name="request_status_changes",
    )

    remarks = models.TextField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "request_status_history"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.service_request.request_number} - {self.status}"