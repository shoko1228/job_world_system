from django.urls import path, include

from .views.edit_profile import EditProfileView
from .views.edit_company_profile import EditCompanyProfileView
from .views.profile import ProfileView
from .views.company_profile import CompanyProfileView

app_name = "users"
urlpatterns = [
    path("edit_profile", EditProfileView.as_view(), name="edit_profile"),
    path("edit_company_profile", EditCompanyProfileView.as_view(), name="edit_company_profile"),
    path("profile", ProfileView.as_view(), name="profile"),
    path("company_profile", CompanyProfileView.as_view(), name="company_profile")
]