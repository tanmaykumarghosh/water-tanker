from django.db import models

from apps.accounts.models import User


class AuditLog(models.Model):

    id = models.BigAutoField(primary_key=True)

    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        db_column="user_id",
        related_name="audit_logs",
    )

    action = models.CharField(
        max_length=100,
    )

    table_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    record_id = models.BigIntegerField(
        blank=True,
        null=True,
    )

    ip_address = models.GenericIPAddressField(
        protocol="both",
        unpack_ipv4=True,
        blank=True,
        null=True,
    )

    user_agent = models.TextField(
        blank=True,
        null=True,
    )

    old_values = models.JSONField(
        blank=True,
        null=True,
    )

    new_values = models.JSONField(
        blank=True,
        null=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "audit_logs"
        managed = False
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.action} ({self.id})"