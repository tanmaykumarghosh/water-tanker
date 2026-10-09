from django.db import transaction

from apps.requests.models import ServiceRequest
from apps.requests.services.matching_service import MatchingService
from apps.requests.services.tracking_service import TrackingService
from apps.notifications.services.notification_service import NotificationService
from apps.audit.services.audit_service import AuditService

from datetime import datetime

from apps.requests.enums import (
    RequestStatus,
    RequestEventType,
    NotificationChannel,
    NotificationType,
)


class RequestService:

    @classmethod
    @transaction.atomic
    def create(cls, *, requester, data, request=None):
        """
        Complete request creation workflow.
        """

        # 1. Generate Request Number
        request_number = cls.generate_request_number()

        # 2. Create Service Request
        service_request = cls.create_request(
            requester=requester,
            request_number=request_number,
            data=data,
        )

        # 3. Initial Status
        TrackingService.add_status(
            service_request=service_request,
            status=RequestStatus.NEW,
            changed_by=requester,
            remarks="Request created",
        )

        # 4. Initial Event
        TrackingService.add_event(
            service_request=service_request,
            event_type=RequestEventType.REQUEST_CREATED,
            user=requester,
            title="Request Created",
            description="Service request created successfully.",
        )

        # 5. Find Matching Users
        recipients = MatchingService.match(service_request)

        # 6. Notify Recipients
        for recipient in recipients:

            NotificationService.notify(
                recipient=recipient,
                service_request=service_request,
                title="New Service Request",
                message=f"Request {service_request.request_number} is available.",
                notification_type=NotificationType.NEW_REQUEST,
            )

        # 7. Audit Log
        AuditService.log(
            user=requester,
            action="CREATE_REQUEST",
            table_name="service_requests",
            record_id=service_request.id,
            ip_address=request.META.get("REMOTE_ADDR") if request else None,
            user_agent=request.META.get("HTTP_USER_AGENT") if request else None,
            new_values={
                "request_number": service_request.request_number,
                "status": service_request.status,
            },
        )

        return service_request
    
    @classmethod
    def create_request(cls, *, requester, request_number, data):

        return ServiceRequest.objects.create(
            requester_user=requester,
            request_number=request_number,
            **data,
        )
    
   


    @classmethod
    def generate_request_number(cls):

        today = datetime.now().strftime("%Y%m%d")

        last = (
            ServiceRequest.objects
            .filter(request_number__startswith=f"REQ-{today}")
            .order_by("-id")
            .first()
        )

        if last:

            last_number = int(last.request_number.split("-")[-1])

            next_number = last_number + 1

        else:

            next_number = 1

        return f"REQ-{today}-{next_number:06d}"
    
    @classmethod
    def update(cls, request_obj, data):
        pass

    @classmethod
    def cancel(cls, request_obj):
        pass

    @classmethod
    def expire(cls, request_obj):
        pass

    @classmethod
    def close(cls, request_obj):
        pass