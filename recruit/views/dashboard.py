from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages

from app.const import USER_TYPE
from ..models import ItemModel, UserFavoriteItemModel,ComFavoriteUserModel,MatchingrModel,ChatMessageModel
from users.models import NormalUser,CompanyUser

app_name = "recruit"

class DashboardView(TemplateView):
    template_name = f"{app_name}/dashboard.html"
    
    def get(self, request):
        #ログインしてなければLP
        if request.user.is_anonymous:
            return redirect("index")
        #ログインしていて、企業ユーザなら企業のHOME
        if request.user.user_type == USER_TYPE.COMPANY_USER:
            return redirect("users:edit_company_profile")
        #ログインしていて、一般ユーザなら、このまま一般のHOME 
        if request.user.normal_user and request.user.user_type == USER_TYPE.NORMAL_USER:
            #管理者とのmatching生成　会員登録時に生成するには、モデルの構造の変更必要
            com_user = CompanyUser.objects.filter(company_name="カウンセラー").first()
            MatchingrModel.objects.get_or_create(
                    normal_user = request.user.normal_user, 
                    com_user = com_user
                )
            first_message = ChatMessageModel.objects.filter(com_user = com_user,normal_user = request.user.normal_user).first()
            if not first_message:
                ChatMessageModel.objects.create(
                    from_user = 1,
                    normal_user = request.user.normal_user, 
                    com_user = com_user,
                    message = "なんでもご相談ください"
                )

            if request.user.normal_user.is_blank():
                messages.info(request, "まず初めにプロフィールを登録してください")
                return redirect("users:edit_profile")
            else:
                favorite_item_list = []
                favorite_items = UserFavoriteItemModel.objects.filter(normal_user=request.user.normal_user).all()
                favorite_item_list = [favorite_item.item_id for favorite_item in favorite_items]     

                #おすすめ一覧　いいねボタンに、「いいね済」か
                items_feature = ItemModel.objects.filter(feature_flag=1)
                for item in items_feature:
                    item.is_favorited = False
                    if item.id in favorite_item_list:
                        item.is_favorited = True

                #自分がいいねした一覧　いいねボタンに、「いいね済」か
                for item in favorite_items:
                    item.is_favorited = True

                #企業から自分にいいね一覧　いいねボタンに、「いいね済」か
                com_favorite_users = ComFavoriteUserModel.objects.filter(normal_user=request.user.normal_user).all()

                                
                return  self.render_to_response({
                    "items_feature":items_feature,
                    "favorite_items":favorite_items,
                    "com_favorite_users":com_favorite_users
                })
        

    
