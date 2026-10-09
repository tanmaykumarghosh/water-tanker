from django.conf import settings
from django.db import models

from apps.requests.models.request_allocation import RequestAllocation


class DeliveryProof(models.Model):

    id = models.BigAutoField(primary_key=True)

    allocation = models.OneToOneField(
        RequestAllocation,
        on_delete=models.CASCADE,
        db_column="allocation_id",
        related_name="delivery_proof",
    )

    customer_photo = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )

    customer_signature = models.CharField(
        max_length=500,
        blank=True,
        null=True,
    )

    remarks = models.TextField(
        blank=True,
        null=True,
    )

    uploaded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        db_column="uploaded_by_id",
        related_name="delivery_proofs",
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        db_table = "delivery_proofs"
        managed = False
        ordering = ["-created_at"]

    def __str__(self):
        return f"Delivery Proof #{self.id}"