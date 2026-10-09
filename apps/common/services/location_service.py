from apps.common.models import Country, Province, District


class LocationService:

    @classmethod
    def countries(cls):

        return (
            Country.objects
            .all()
            .order_by("name")
        )

    @classmethod
    def provinces(cls, country_id):

        queryset = (
            Province.objects
            .all()
            .order_by("name")
        )

        if country_id:
            queryset = queryset.filter(
                country_id=country_id
            )

        return queryset

    @classmethod
    def districts(cls, province_id):

        queryset = (
            District.objects
            .all()
            .order_by("name")
        )

        if province_id:
            queryset = queryset.filter(
                province_id=province_id
            )

        return queryset