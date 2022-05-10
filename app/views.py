from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from recruit.models import ItemModel, UserFavoriteItemModel
from app.const import USER_TYPE


class IndexView(TemplateView):
    template_name = "index.html"

    def get(self, request):
        items_feature = ItemModel.objects.filter(feature_flag=1)
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
            "items_feature":items_feature
        })
    
    
class LoginRequiredView(TemplateView):
    template_name = "login_required.html"

        
class CancelView(TemplateView):
    template_name = "cancel.html"