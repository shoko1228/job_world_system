from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages

from app.const import USER_TYPE
from ..models import ItemModel, UserFavoriteItemModel

app_name = "recruit"

class DashboardView(TemplateView):
    template_name = f"{app_name}/dashboard.html"
    
    def get(self, request):
        if request.user.is_anonymous:
            return self.render_to_response({})
        if request.user.user_type == USER_TYPE.COMPANY_USER:
            return redirect("users:edit_company_profile")
        if request.user.normal_user and request.user.user_type == USER_TYPE.NORMAL_USER:
            if request.user.normal_user.is_blank():
                messages.info(request, "まず初めにプロフィールを登録してください")
                return redirect("users:edit_profile")


        items_feature = ItemModel.objects.filter(feature_flag=1)
        for item in items_feature:
            item.is_favorited = False
            if self.request.user.is_authenticated:
                if request.user.user_type == USER_TYPE.NORMAL_USER:
                    favorite_items = UserFavoriteItemModel.objects.filter(user=request.user).all()
                    for favorite_item in favorite_items:
                        if item.id == favorite_item.item_id:
                            item.is_favorited = True
                            break
        
        items_user_like= UserFavoriteItemModel.objects.filter(usre_id=request.user)
        # for item in items_feature:
        #     item.is_favorited = False
        #     if self.request.user.is_authenticated:
        #         if request.user.user_type == USER_TYPE.NORMAL_USER:
        #             favorite_items = UserFavoriteItemModel.objects.filter(user=request.user).all()
        #             for favorite_item in favorite_items:
        #                 if item.id == favorite_item.item_id:
        #                     item.is_favorited = True
        #                     break

                         
        return  self.render_to_response({
            "items_feature":items_feature,
            "items_user_like":items_user_like
        })
        

    
