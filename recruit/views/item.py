from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import ItemModel, UserFavoriteItemModel
from ..forms.item import ItemSearchForm
from app.const import USER_TYPE


app_name = "recruit"

class ItemView(TemplateView):
    template_name = f"{app_name}/item.html"
    
    def get(self, request):
        items = ItemModel.objects.all().order_by("created_at")
        form = ItemSearchForm(request.GET)
        items = form.filter_items(items)
        item_cnt = len(items)
        
        favorite_item_list = []
        if self.request.user.is_authenticated:
            if request.user.user_type == USER_TYPE.NORMAL_USER:
                favorite_items = UserFavoriteItemModel.objects.filter(normal_user=request.user.normal_user).all()
                favorite_item_list = [favorite_item.item_id for favorite_item in favorite_items]
        
        for item in items:
            item.is_favorited = False
            if self.request.user.is_authenticated:
                if request.user.user_type == USER_TYPE.NORMAL_USER:
                    if item.id in favorite_item_list:
                        item.is_favorited = True


        items_feature = ItemModel.objects.filter(feature_flag=1)
        for item in items_feature:
            item.is_favorited = False
            if self.request.user.is_authenticated:
                if request.user.user_type == USER_TYPE.NORMAL_USER:
                    if item.id in favorite_item_list:
                        item.is_favorited = True
  
        params = request.GET.copy()
        if 'page' in params:
            page = params['page']
            del params['page']
        else:
            page = 1
        search_params = params.urlencode()
        
        paginator = Paginator(items, 5)
        try:
            items = paginator.page(page)
        except (EmptyPage, PageNotAnInteger):
            items = paginator.page(1)

        return  self.render_to_response({
            "items":items,
            "item_cnt":item_cnt,
            "form":form,
            "search_params":search_params,
            "items_feature":items_feature
        })