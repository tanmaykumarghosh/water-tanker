from apps.profiles.models import ProviderProfile


class ProviderService:

    @staticmethod
    def get_provider(user):
        return ProviderProfile.objects.filter(user=user).first()

    @staticmethod
    def increase_contract_count(provider):
        provider.total_contracts += 1
        provider.save(update_fields=["total_contracts"])