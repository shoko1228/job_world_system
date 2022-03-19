from django.shortcuts import render, redirect
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.http import Http404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from ..forms.normal_user import NormalUserForm
from app.const import USER_TYPE
from app.const import CHOICES

app_name = "users"

@method_decorator(login_required, name="dispatch")
class ProfileView(TemplateView):
    template_name = f"{app_name}/profile.html"
    
    def get(self, request):
        if not request.user.user_type == USER_TYPE.NORMAL_USER:
            raise Http404("企業アカウントは、このページは表示できません")
        print(request.user.normal_user)
        normal_user = request.user.normal_user
        normal_user.status = CHOICES.STATUS[normal_user.status][1]
        normal_user.gender = CHOICES.GENDER[normal_user.gender][1]
        normal_user.education_status = CHOICES.EDUCATION_STATUS[normal_user.education_status][1]
        normal_user.school_type = CHOICES.SCHOOL_TYPE[normal_user.school_type][1]
        
        #form = NormalUserForm(instance=request.user.normal_user)
        return self.render_to_response({"normal_user": normal_user})
    