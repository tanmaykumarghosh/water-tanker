import uuid

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):

    def create_user(self, phone, password=None, **extra_fields):

        if not phone:
            raise ValueError("Phone number is required")

        if not extra_fields.get("first_name"):
            raise ValueError("First name is required")

        user = self.model(phone=phone, **extra_fields)

        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_superuser(self, phone, password=None, **extra_fields):

        extra_fields.setdefault("role", "ADMIN")
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        return self.create_user(phone, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):

    class Role(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        CUSTOMER = "CUSTOMER", "Customer"
        PROVIDER = "PROVIDER", "Provider"
        DRIVER = "DRIVER", "Driver"

    class Status(models.TextChoices):
        ACTIVE = "ACTIVE", "Active"
        INACTIVE = "INACTIVE", "Inactive"
        SUSPENDED = "SUSPENDED", "Suspended"

    id = models.BigAutoField(primary_key=True)

    uuid = models.UUIDField(default=uuid.uuid4, unique=True)

    first_name = models.CharField(max_length=100)

    middle_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    last_name = models.CharField(
        max_length=100,
        blank=True,
        null=True,
    )

    phone = models.CharField(max_length=20, unique=True)

    email = models.EmailField(blank=True, null=True, unique=True)

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.PROVIDER,
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.ACTIVE,
    )

    phone_verified = models.BooleanField(default=False)

    email_verified = models.BooleanField(default=False)

    is_staff = models.BooleanField(default=False)

    is_superuser = models.BooleanField(default=False)

    is_active = models.BooleanField(default=True)

    last_login = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = "phone"

    REQUIRED_FIELDS = []

    class Meta:
        db_table = "users"

    @property
    def full_name(self):
        return " ".join(
            filter(
                None,
                [
                    self.first_name,
                    self.middle_name,
                    self.last_name,
                ],
            )
        )

    def __str__(self):
        return  self.phone or self.full_name