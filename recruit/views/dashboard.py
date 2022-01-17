from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.contrib import messages

from app.const import USER_TYPE

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
        
        return self.render_to_response({})
    
