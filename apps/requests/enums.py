from django.db import models


class RequestType(models.TextChoices):
    INSTANT = "INSTANT", "Instant"
    CONTRACT = "CONTRACT", "Contract"


class FulfillmentType(models.TextChoices):
    FULL = "SINGLE_DRIVER", "Single Driver"
    PARTIAL = "MULTIPLE_DRIVERS", "Multiple Drivers"


class ServiceType(models.TextChoices):
    WATER = "WATER", "Water"
    SEPTIC = "SEPTIC", "Septic"

class TankerStatus(models.TextChoices):
    AVAILABLE = "AVAILABLE", "Available"
    BUSY = "BUSY", "Busy"
    MAINTENANCE = "MAINTENANCE", "Maintenance"
    OFFLINE = "OFFLINE", "Offline"


class RequestStatus(models.TextChoices):
    NEW = "NEW", "New"
    # MATCHED = "MATCHED", "Matched"
    # QUOTATION_RECEIVED = "QUOTATION_RECEIVED", "Quotation Received"
    # ALLOCATED = "ALLOCATED", "Allocated"
    # ACCEPTED = "ACCEPTED", "Accepted"
    WAITING_ASSIGNMENT = "WAITING_ASSIGNMENT", "Waiting Assigned"
    ASSIGNED = "ASSIGNED", "Assigned"
    ON_THE_WAY = "ON_THE_WAY", "On The Way"
    # DEPARTED = "DEPARTED", "Departed"
    DELIVERY_STARTED = "DELIVERY_STARTED", "Delivery Started"
    COMPLETED = "COMPLETED", "Completed"
    CANCELLED = "CANCELLED", "Cancelled"
    # EXPIRED = "EXPIRED", "Expired"

   


class QuotationStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    ACCEPTED = "ACCEPTED", "Accepted"
    REJECTED = "REJECTED", "Rejected"
    EXPIRED = "EXPIRED", "Expired"


class AllocationStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    ARRIVED = "ARRIVED", "Arrived"
    ACCEPTED = "ACCEPTED", "Accepted"
    REJECTED = "REJECTED", "Rejected"
    ON_THE_WAY = "ON_THE_WAY", "Delivery Started"
    DELIVERY_STARTED = "DELIVERY_STARTED", "Delivery Started"
    DELIVERED = "DELIVERED", "Delivered"
    CANCELLED = "CANCELLED", "Cancelled"

class TrackingStatus(models.TextChoices):
    ON_THE_WAY = "ON_THE_WAY", "On The Way"
    ARRIVED = "ARRIVED", "Arrived"
    DELIVERY_STARTED = "DELIVERY_STARTED", "Delivery Started"
    DELIVERED = "DELIVERED", "Delivered"


class OTPStatus(models.TextChoices):
    PENDING = "PENDING", "Pending"
    VERIFIED = "VERIFIED", "Verified"
    EXPIRED = "EXPIRED", "Expired"


class ProofType(models.TextChoices):
    PHOTO = "PHOTO", "Photo"
    SIGNATURE = "SIGNATURE", "Signature"

class NotificationChannel(models.TextChoices):
    APP = "APP", "App"
    WHATSAPP = "WHATSAPP", "WhatsApp"
    SMS = "SMS", "SMS"
    EMAIL = "EMAIL", "Email"

class NotificationType(models.TextChoices):
    NEW_REQUEST = "NEW_REQUEST", "New Request"
    REQUEST_ACCEPTED = "REQUEST_ACCEPTED", "Request Accepted"
    NEW_QUOTATION = "NEW_QUOTATION", "New Quotation"
    QUOTATION_ACCEPTED = "QUOTATION_ACCEPTED", "Quotation Accepted"
    STATUS_UPDATED = "STATUS_UPDATED", "Status Updated"
    SYSTEM = "SYSTEM", "System"


class NotificationStatus(models.TextChoices):
    UNREAD = "UNREAD", "Unread"
    READ = "READ", "Read"

class RecipientResponse(models.TextChoices):
    PENDING = "PENDING", "Pending"
    VIEWED = "VIEWED", "Viewed"
    ACCEPTED = "ACCEPTED", "Accepted"
    REJECTED = "REJECTED", "Rejected"
    NO_RESPONSE = "NO_RESPONSE", "No Response"
    EXPIRED = "EXPIRED", "Expired"

class RequestEventType(models.TextChoices):
    REQUEST_CREATED = "REQUEST_CREATED", "Request Created"
    REQUEST_UPDATED = "REQUEST_UPDATED", "Request Updated"
    TARGETS_MATCHED = "TARGETS_MATCHED", "Targets Matched"
    RECIPIENTS_SELECTED = "RECIPIENTS_SELECTED", "Recipients Selected"
    NOTIFICATION_SENT = "NOTIFICATION_SENT", "Notification Sent"
    NOTIFICATION_DELIVERED = "NOTIFICATION_DELIVERED", "Notification Delivered"
    REQUEST_VIEWED = "REQUEST_VIEWED", "Request Viewed"
    QUOTATION_SUBMITTED = "QUOTATION_SUBMITTED", "Quotation Submitted"
    QUOTATION_UPDATED = "QUOTATION_UPDATED", "Quotation Updated"
    QUOTATION_ACCEPTED = "QUOTATION_ACCEPTED", "Quotation Accepted"
    QUOTATION_REJECTED = "QUOTATION_REJECTED", "Quotation Rejected"
    ALLOCATION_CREATED = "ALLOCATION_CREATED", "Allocation Created"
    DRIVER_ACCEPTED = "DRIVER_ACCEPTED", "Driver Accepted"
    DRIVER_REJECTED = "DRIVER_REJECTED", "Driver Rejected"
    DRIVER_ON_THE_WAY = "DRIVER_ON_THE_WAY", "Driver On The Way"
    DELIVERY_STARTED = "DELIVERY_STARTED", "Delivery Started"
    DELIVERY_COMPLETED = "DELIVERY_COMPLETED", "Delivery Completed"
    REQUEST_CANCELLED = "REQUEST_CANCELLED", "Request Cancelled"
    SYSTEM_EVENT = "SYSTEM_EVENT", "System Event"