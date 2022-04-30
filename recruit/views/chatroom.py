from django.shortcuts import render,redirect
from django.urls import reverse
from urllib.parse import urlencode
from django.http.response import HttpResponse
from django.views.generic import TemplateView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

from ..models import MatchingrModel,ChatMessageModel
from ..forms.chat_message import ChatMessageForm
from app.const import USER_TYPE
from django.http import Http404


app_name = "recruit"

class ChatroomView(TemplateView):
    template_name = f"{app_name}/chatroom.html"

    
    def get(self, request):
        matching = MatchingrModel.objects.filter(id=request.GET.get("id")).first()
        print(matching)
        if matching:
            chat_message=ChatMessageModel.objects.filter(com_user = matching.com_user, normal_user = matching.normal_user).all().order_by("created_at")
            # form = ChatMessageForm(initial={
            # 'normal_user': matching.normal_user,
            # 'com_user': matching.com_user,
            # 'from_user': request.user.user_type,
            # })
            
            return  self.render_to_response({
                "matching":matching,
                "chat_message":chat_message,
                # "form": form,
            })
        else:
            return Http404("このページは表示できません")
        
        
        #if request.user.user_type == USER_TYPE.NORMAL_USER: #0=normal, 1=company
        #else:
        #chat_message=ChatMessageModel.objects.filter(com_user = com_user).first()
    # def post(self, request):
    #     form = ChatMessageForm(request.POST)
    #     if not form.is_valid():
    #         messages.error(request, "保存に失敗しました")
    #         for field in form:
    #             for error in field.errors:
    #                 messages.error(request, f"{field.label}: {error}")
    #     else:
    #         form.save()
    #         messages.success(request, "保存しました")

    #     matching = MatchingrModel.objects.filter(id=request.GET.get("id")).first()
    #     if matching:
    #         chat_message=ChatMessageModel.objects.filter(com_user = matching.com_user, normal_user = matching.normal_user).all().order_by("created_at")
    #         form = ChatMessageForm()
    #         return  self.render_to_response({
    #             "matching":matching,
    #             "chat_message":chat_message,
    #             "form": form,
    #         })
    #     else:
    #         return Http404("このページは表示できません")
    def post(self, request):
        chat_message = request.POST.get("message")
        matching = MatchingrModel.objects.filter(id=request.POST.get("id")).first()

        if matching:
            chat_message = ChatMessageModel.objects.create(
                normal_user = matching.normal_user,
                com_user = matching.com_user,
                message = chat_message,
                from_user = request.user.user_type,            
                )


        redirect_url = reverse("recruit:chatroom")
        parameters = urlencode({'id': request.POST.get("id")})
        url = f'{redirect_url}?{parameters}'
            
        return redirect(url)
        if matching:
            form = ChatMessageForm(initial={
                'normal_user': matching.normal_user,
                'com_user': matching.com_user,
                'from_user': request.user.user_type,
                'message': message,
                })
            
            print(form)

            if not form.is_valid():
                messages.error(request, "保存に失敗しました")
                for field in form:
                    for error in field.errors:
                        messages.error(request, f"{field.label}: {error}")
            else:
                form.save()
                messages.success(request, "保存しました")


        if matching:
            chat_message=ChatMessageModel.objects.filter(com_user = matching.com_user, normal_user = matching.normal_user).all().order_by("created_at")
            return  self.render_to_response({
                "matching":matching,
                "chat_message":chat_message,
            })
        else:
            return Http404("このページは表示できません")
