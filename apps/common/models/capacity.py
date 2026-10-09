from django.db import models


    
class Capacity(models.Model):
    id = models.BigAutoField(primary_key=True)

    liters = models.IntegerField(unique=True)

    display_name = models.CharField(max_length=30)

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "capacities"
        managed = False
        ordering = ["liters"]
        verbose_name = "Capacity"
        verbose_name_plural = "Capacities"

    def __str__(self):
        return self.display_name