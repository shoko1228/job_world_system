from django.urls import path, include

from .views.edit_profile import EditProfileView
from .views.edit_company_profile import EditCompanyProfileView

app_name = "users"
urlpatterns = [
    path("edit_profile", EditProfileView.as_view(), name="edit_profile"),
    path("edit_company_profile", EditCompanyProfileView.as_view(), name="edit_company_profile")
]