from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..forms.normal_user import NormalUserForm
from app.const import USER_TYPE
from app.const import CHOICES
from recruit.models import UserFavoriteItemModel,ComFavoriteUserModel,ItemModel

app_name = "users"

@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    template_name = f"{app_name}/profile.html"
    
    def get(self, request):
        if not request.user.user_type == USER_TYPE.NORMAL_USER:
            raise Http404("企業アカウントは、このページは表示できません")
        print(request.user.normal_user)
        normal_user = request.user.normal_user
        normal_user.status = CHOICES.STATUS[normal_user.status][1]
        normal_user.gender = CHOICES.GENDER[normal_user.gender][1]
        normal_user.education_status = CHOICES.EDUCATION_STATUS[normal_user.education_status][1]
        normal_user.school_type = CHOICES.SCHOOL_TYPE[normal_user.school_type][1]


        user_favorite_items = UserFavoriteItemModel.objects.filter(normal_user=request.user.normal_user).all()

        favorite_item_list = [favorite_item.item_id for favorite_item in user_favorite_items]


        #ひとまずcreated_atの1件目を「企業からのいいね」に表示。表示用のデフォルト選ぶか、他の求人も一覧観れるようにするか。
        com_favorite_users = ComFavoriteUserModel.objects.filter(normal_user=request.user.normal_user).all()
        com_favorite_users_items=[]
        for com_favorite_user in com_favorite_users:
            item = ItemModel.objects.all().filter(company=com_favorite_user.com_user).order_by("created_at").first()
            com_favorite_users_items.append(item)
        
        for item in com_favorite_users_items:
            item.is_favorited = False
            if item.id in favorite_item_list:
                item.is_favorited = True

        #「企業からのいいね」に企業全ての求人を表示するなら下記
        # com_favorite_users_list = [com_favorite_user.com_user for com_favorite_user in com_favorite_users]
        # items = ItemModel.objects.all().order_by("created_at")
        # com_favorite_users_items=[]
        # for item in items:
        #     if item.company in com_favorite_users_list:
        #         item.is_favorited = False
        #         com_favorite_users_items.append(item)
        #         if item.id in favorite_item_list:
        #             item.is_favorited = True
        
        #form = NormalUserForm(instance=request.user.normal_user)
        return self.render_to_response({
            "normal_user": normal_user,
            "user_favorite_items":user_favorite_items,
            "com_favorite_users_items":com_favorite_users_items

        })
    