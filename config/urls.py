from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),

    # ------------------------------------------------------------------
    # API v1
    # ------------------------------------------------------------------

    path(
        "api/v1/accounts/",
        include("apps.accounts.api.urls"),
    ),

    path(
        "api/v1/customer/",
        include("apps.customer.api.urls"),
    ),

    path(
        "api/v1/driver/",
        include("apps.driver.api.urls"),
    ),

    path(
        "api/v1/profiles/",
        include("apps.profiles.api.urls"),
    ),

    path(
        "api/v1/requests/",
        include("apps.requests.api.urls"),
    ),

    path(
        "api/v1/notifications/",
        include("apps.notifications.api.urls"),
    ),
    path(
        "api/v1/customer/",
        include("apps.customer.api.urls"),
    ),
    path(
        "api/v1/common/",
        include("apps.common.api.urls"),
    ),
    
]