from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import ItemModel, UserFavoriteItemModel
from ..forms.item import ItemSearchForm
from app.const import USER_TYPE


app_name = "recruit"

class ChatView(TemplateView):
    template_name = f"{app_name}/chat.html"
    
    def get(self, request):


        return  self.render_to_response({

        })