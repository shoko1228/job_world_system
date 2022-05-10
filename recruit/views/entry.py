from asyncio import FastChildWatcher
from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView,DetailView

from ..models import ItemModel, UserFavoriteItemModel
from ..forms.item import ItemSearchForm
from app.const import USER_TYPE
from django.http import Http404


app_name = "recruit"

# class ItemDetailView(DetailView):
#     template_name = f"{app_name}/item_detail.html"

#     model = ItemModel


class EntryView(TemplateView):
    template_name = f"{app_name}/entry.html"
    
    def get(self, request):
        item = ItemModel.objects.filter(id=request.GET.get("id")).first()    
          
        #そのIDのitem無いときなど、他のページに戻す処理
        if not item:
            return Http404("このページは表示できません")

        return self.render_to_response({
            "item": item
        })