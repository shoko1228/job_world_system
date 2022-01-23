from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import ItemModel, UserFavoriteItemModel
from ..forms.item import ItemSearchForm


app_name = "recruit"

class SearchUserView(TemplateView):
    template_name = f"{app_name}/search_user.html"
    
    # def get(self, request):
    #     items = ItemModel.objects.all()
    #     form = ItemSearchForm(request.GET)
    #     items = form.filter_items(items)
    #     item_cnt = len(items)
        
    #     favorite_items = UserFavoriteItemModel.objects.filter(user=request.user).all()
    #     for item in items:
    #         item.is_favorited = False
    #         for favorite_item in favorite_items:
    #             if item.id == favorite_item.item_id:
    #                 item.is_favorited = True
    #                 break
  
    #     params = request.GET.copy()
    #     if 'page' in params:
    #         page = params['page']
    #         del params['page']
    #     else:
    #         page = 1
    #     search_params = params.urlencode()
        
    #     paginator = Paginator(items, 5)
    #     try:
    #         items = paginator.page(page)
    #     except (EmptyPage, PageNotAnInteger):
    #         items = paginator.page(1)

    #     return  self.render_to_response({
    #         "items":items,
    #         "item_cnt":item_cnt,
    #         "form":form,
    #         "search_params":search_params
    #     })