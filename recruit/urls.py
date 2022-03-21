from django.urls import path, include
from rest_framework import routers


# from .serializers.item import ItemSerializer
from .view_sets.item import ItemViewSet
from .views.dashboard import DashboardView
from .views.company_dashboard import CompanyDashboardView
from .views.item import ItemView
from .views.search_user import SearchUserView
from .views.item_detail import ItemDetailView
from .views.api.user_favorite_item import UserFavoriteItemAPIView
from .views.api.com_favorite_user import ComFavoriteUserAPIView

app_name = "recruit"
urlpatterns = [
    path('dashboard', DashboardView.as_view(), name="dashboard"),
    path('company_dashboard', CompanyDashboardView.as_view(), name="company_dashboard"),
    path('item', ItemView.as_view(), name="item"),
    path('item_detail', ItemDetailView.as_view(), name="item_detail"),
    #path('item_detail/<int:pk>/', ItemDetailView.as_view(), name='item_detail'),
    path(r'api/item_favorite', UserFavoriteItemAPIView.as_view()),
    path(r'api/user_favorite', ComFavoriteUserAPIView.as_view()),
    path('search_user', SearchUserView.as_view(), name="search_user"),
]
