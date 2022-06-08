from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..forms.company_user import CompanyUserForm
from app.const import USER_TYPE
from recruit.models import UserFavoriteItemModel,ComFavoriteUserModel,ItemModel
from ..models import NormalUser
from app.const import CHOICES

app_name = "users"

@method_decorator(login_required, name="dispatch")
class CompanyProfileView(TemplateView):
    template_name = f"{app_name}/company_profile.html"
    
    # def get(self, request):
    #     if not request.user.user_type == USER_TYPE.COMPANY_USER:
    #         return Http404("一般ユーザーアカウントは、このページは表示できません")
    #     company_user = request.user.company_user
    #     #form = CompanyUserForm(instance=request.user.company_user)
    #     return self.render_to_response({"company_user": company_user})

    def get(self, request):
        if request.user.is_anonymous:
            return self.render_to_response({})
        if not request.user.user_type == USER_TYPE.COMPANY_USER:
            return Http404("一般ユーザーアカウントは、このページは表示できません")
        if request.user.company_user and request.user.user_type == USER_TYPE.COMPANY_USER:
            if request.user.company_user.is_blank():
                messages.info(request, "まず初めにプロフィールを登録してください")
                return redirect("users:edit_company_profile")
        company_user = request.user.company_user
        
        #return self.render_to_response({"company_user": company_user})


        favorite_item_list = []
        favorite_items = UserFavoriteItemModel.objects.filter(normal_user=request.user.normal_user).all()
        favorite_item_list = [favorite_item.item_id for favorite_item in favorite_items]     
        
        favorite_user_list = []
        favorite_users = ComFavoriteUserModel.objects.filter(com_user=request.user.company_user).all()
        favorite_user_list = [favorite_user.normal_user_id for favorite_user in favorite_users]


        #おすすめ一覧　いいねボタンに、「いいね済」か
        # items_feature = ItemModel.objects.filter(feature_flag=1)
        # for item in items_feature:
        #     item.is_favorited = False
        #     if item.id in favorite_item_list:
        #         item.is_favorited = True

        #自社がいいねした一覧　いいねボタンに、「いいね済」か（もちろん全てtrue）
        for favorite_user in favorite_users:
            favorite_user.is_favorited = True
            favorite_user.normal_user.status = CHOICES.STATUS[favorite_user.normal_user.status][1]
            favorite_user.normal_user.gender = CHOICES.GENDER[favorite_user.normal_user.gender][1]
            favorite_user.normal_user.education_status = CHOICES.EDUCATION_STATUS[favorite_user.normal_user.education_status][1]
            favorite_user.normal_user.school_type = CHOICES.SCHOOL_TYPE[favorite_user.normal_user.school_type][1]

        #求職者から自社にいいね一覧　いいねボタンに、「いいね済」か
        user_favorite_coms = UserFavoriteItemModel.objects.filter(item__company=request.user.company_user).all()
        for user_favorite_com in user_favorite_coms:
            user_favorite_com.normal_user.status = CHOICES.STATUS[user_favorite_com.normal_user.status][1]
            user_favorite_com.normal_user.gender = CHOICES.GENDER[user_favorite_com.normal_user.gender][1]
            user_favorite_com.normal_user.education_status = CHOICES.EDUCATION_STATUS[user_favorite_com.normal_user.education_status][1]
            user_favorite_com.normal_user.school_type = CHOICES.SCHOOL_TYPE[user_favorite_com.normal_user.school_type][1]
            user_favorite_com.is_favorited = False
            if user_favorite_com.normal_user.id in favorite_user_list:
                user_favorite_com.is_favorited = True
                        
        return  self.render_to_response({
            "company_user":company_user,
            "user_favorite_coms":user_favorite_coms,
            "favorite_users":favorite_users
        })