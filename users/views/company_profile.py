from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..forms.company_user import CompanyUserForm
from app.const import USER_TYPE

app_name = "users"

@method_decorator(login_required, name="dispatch")
class CompanyProfileView(TemplateView):
    template_name = f"{app_name}/company_profile.html"
    
    def get(self, request):
        if not request.user.user_type == USER_TYPE.COMPANY_USER:
            return Http404("一般ユーザーアカウントは、このページは表示できません")
        company_user = request.user.company_user
        #form = CompanyUserForm(instance=request.user.company_user)
        return self.render_to_response({"company_user": company_user})