from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

from .models import *
from .forms.normal_user import NormalUserForm
from app.const import USER_TYPE


class AccountAdapter(DefaultAccountAdapter):
    '''
    Userアカウントに紐づける処理を定義できるクラス
    '''

    def save_user(self, request, user, form, commit=True):
        '''
        ユーザー登録時に実行される
        ユーザー登録時に一般ユーザーと企業ユーザーで異なる処理を実装する
        '''
        # 継承元の処理を行い、ユーザーを作成
        super(AccountAdapter, self).save_user(request, user, form, commit=False)
        user.user_type = int(request.POST.get("user_type", 0))
        print(user.user_type)
        
        # 一般ユーザー個別処理
        if user.user_type == USER_TYPE.NORMAL_USER:
            # 一般ユーザー用テーブルを作成
            user_attribute = NormalUser()
            user_attribute.save()
            user.normal_user = user_attribute
        # 企業ユーザー個別処理
        else:
            user_attribute = CompanyUser()
            user_attribute.save()
            user.company_user = user_attribute
        
        user.save()

    
    def get_login_redirect_url(self, request):
        '''
        ログイン後のリダイレクト先をUserTypeで振り分ける
        '''
        # user_type=1の場合は企業ユーザー用、それ以外は一般ユーザー用のリダイレクトURLを返す
        if request.user.user_type == USER_TYPE.COMPANY_USER:
            return settings.LOGIN_REDIRECT_URL_COMPANY 
        else:
            return super().get_login_redirect_url(request)
