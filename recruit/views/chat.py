from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from ..models import MatchingrModel
from ..forms.item import ItemSearchForm
from app.const import USER_TYPE


app_name = "recruit"

class ChatView(TemplateView):
    template_name = f"{app_name}/chat.html"
    
    def get(self, request):
        matching_list = []
        if self.request.user.is_authenticated:
            if request.user.user_type == USER_TYPE.NORMAL_USER: #0=normal, 1=company
                matching_list = MatchingrModel.objects.filter(normal_user=request.user.normal_user).exclude(delete_flg=1).all()#orderは新規チャット順？delete一応チャックしとく
            else:
                matching_list = MatchingrModel.objects.filter(com_user=request.user.company_user).exclude(delete_flg=1).all()



        return  self.render_to_response({
            "matching_list":matching_list,
            
        })