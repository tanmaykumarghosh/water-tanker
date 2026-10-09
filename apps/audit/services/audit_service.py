from apps.audit.models import AuditLog


class AuditService:

    @staticmethod
    def log(
        *,
        user=None,
        action,
        table_name=None,
        record_id=None,
        ip_address=None,
        user_agent=None,
        old_values=None,
        new_values=None,
    ):
        return AuditLog.objects.create(
            user=user,
            action=action,
            table_name=table_name,
            record_id=record_id,
            ip_address=ip_address,
            user_agent=user_agent,
            old_values=old_values,
            new_values=new_values,
        )