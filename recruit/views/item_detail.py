from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView,DetailView

from ..models import ItemModel, UserFavoriteItemModel
from ..forms.item import ItemSearchForm


app_name = "recruit"

# class ItemDetailView(DetailView):
#     template_name = f"{app_name}/item_detail.html"

#     model = ItemModel


class ItemDetailView(TemplateView):
    template_name = f"{app_name}/item_detail.html"
    
    def get(self, request):
        item = ItemModel.objects.filter(id=request.GET.get("id")).first()
        #todo if そのIDのitem無いときなど、他のページに戻す処理


        return self.render_to_response({
            "item": item
        })