from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import ItemModel, UserFavoriteItemModel, ComFavoriteUserModel
from ..forms.item import ItemSearchForm
from users.models import NormalUser
from app.const import CHOICES
from app.const import USER_TYPE


app_name = "recruit"

class SearchUserView(TemplateView):
    template_name = f"{app_name}/search_user.html"

    def get(self, request):
        normal_users = NormalUser.objects.all()
        user_cnt = len(normal_users)

        favorite_user_list = []
        if self.request.user.is_authenticated:
            if request.user.user_type == USER_TYPE.COMPANY_USER:
                favorite_users = ComFavoriteUserModel.objects.filter(com_user=request.user.company_user).all()
                favorite_user_list = [favorite_user.normal_user.id for favorite_user in favorite_users]


        for normal_user in normal_users:
            normal_user.status = CHOICES.STATUS[normal_user.status][1]
            normal_user.gender = CHOICES.GENDER[normal_user.gender][1]
            normal_user.education_status = CHOICES.EDUCATION_STATUS[normal_user.education_status][1]
            normal_user.school_type = CHOICES.SCHOOL_TYPE[normal_user.school_type][1]

            normal_user.is_favorited = False
            if self.request.user.is_authenticated:
                if request.user.user_type == USER_TYPE.COMPANY_USER:
                        if normal_user.id in favorite_user_list:
                            normal_user.is_favorited = True

        


    
        return  self.render_to_response({
            "normal_users":normal_users,
            "user_cnt":user_cnt,
        })
