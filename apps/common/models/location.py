
from django.db import models


class Country(models.Model):
    id = models.BigAutoField(primary_key=True)

    name = models.CharField(max_length=100)

    iso_code = models.CharField(
        max_length=2,
        unique=True,
        blank=True,
        null=True,
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "countries"
        managed = False
        ordering = ["name"]

    def __str__(self):
        return self.name

class Province(models.Model):
    id = models.BigAutoField(primary_key=True)

    country = models.ForeignKey(
        Country,
        on_delete=models.RESTRICT,
        db_column="country_id",
        related_name="provinces",
    )

    name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "provinces"
        managed = False
        ordering = ["country", "name"]

    def __str__(self):
        return f"{self.name} ({self.country.name})"
    
class District(models.Model):
    id = models.BigAutoField(primary_key=True)

    province = models.ForeignKey(
        Province,
        on_delete=models.RESTRICT,
        db_column="province_id",
        related_name="districts",
    )

    name = models.CharField(max_length=100)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "districts"
        managed = False
        ordering = ["province__country__name", "province__name", "name"]

    def __str__(self):
        return f"{self.name}, {self.province.name}"