from django.contrib import admin
from django.contrib.sites.models import Site
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib import admin
from allauth.socialaccount.models import SocialToken, SocialAccount, SocialApp
from recruit.models import *

from .models import NormalUser, CompanyUser

# 不要なアカウントの非表示
admin.site.unregister(Group)
admin.site.unregister(SocialToken)
admin.site.unregister(SocialAccount)
admin.site.unregister(SocialApp)
admin.site.unregister(Site)


# 必要なアカウントの表示設定
@admin.register(get_user_model())
class CustomUserAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('password',)}),
        (_('Personal info'), {'fields': ('username', 'email', 'user_type')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       )})
    )
    list_display = ('email', 'is_staff', 'is_superuser')
    list_filter = []
    search_fields = ('email', 'username')

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    ordering = ('email',)
    
    

@admin.register(NormalUser)
class NormalUserAdmin(admin.ModelAdmin):
    fields = ('nickname', 'last_name', 'first_name')
    list_display = ('nickname', 'last_name', 'first_name')
    ordering = ('nickname',)
    
    
@admin.register(ItemModel)
class ItemModelAdmin(admin.ModelAdmin):
    list_display = ('id','name')

@admin.register(UserFavoriteItemModel)
class UserFavoriteItemModelAdmin(admin.ModelAdmin):
    list_display = ('id','item','user','created_at','delete_flg')
