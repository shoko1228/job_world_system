from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db.models.fields import BLANK_CHOICE_DASH
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
import ulid
from django.core.validators import RegexValidator

from common.models import *
from app.const import USER_TYPE

class CustomUserManager(UserManager):
    '''
    Userを作成するための処理
    Userの項目が変更になっているので、こちらも変更の必要がある
    '''    
    
    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    
    def create_user(self, email=None, password=None, **extra_fields):
        '''
        一般ユーザーを作成する処理
        '''
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)
    
    
    def create_superuser(self, email=None, password=None, **extra_fields):
        '''
        管理者ユーザーを作成する処理
        '''
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)
    
# class LocationUserModel(models.Model):
#     location = models.CharField(verbose_name="都道府県",max_length=64, null=False, blank=False)
#     class Meta:
#         db_table = "location_user"
#         verbose_name = "都道府県"
#         verbose_name_plural = "都道府県"
    
#     def __str__(self):
#         return self.location

# class JobTypeModel(models.Model):
#     job_type = models.CharField(verbose_name="職種",max_length=64, null=False, blank=False)
#     class Meta:
#         db_table = "job_type"
#         verbose_name = "職種"
#         verbose_name_plural = "職種"
    
#     def __str__(self):
#         return self.job_type

class NormalUser(models.Model):
    id = models.CharField(max_length=32, default=ulid.new, primary_key=True, editable=False) 
    # first_name = models.CharField(_('名前'), max_length=32, blank=True)
    # last_name = models.CharField(_('苗字'), max_length=32, blank=True)
    # nickname = models.CharField(_('ニックネーム'), max_length=32, blank=True)
    # gender = models.IntegerField(_('性別'), blank=True, default=0)
    # phone_number = models.CharField(_('電話番号'), max_length=16, blank=True)
    # address = models.TextField(_('住所'), blank=False)
    created_at = models.DateTimeField(verbose_name="作成日時", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="更新日時", auto_now=True)

    pr_message = models.TextField(_('ひと言PR'), max_length=500, null=True, blank=True)
    favorite_thing = models.TextField(_('好きなことは？'), max_length=500,null=True, blank=True)
    status =  models.IntegerField(_('ステータス'), blank=True, default=0)
    image_top = models.ImageField(_('トップ画像'), upload_to='images',null=True, blank=True)
    image1 = models.ImageField(_('画像１'), upload_to='images',null=True, blank=True)
    image2 = models.ImageField(_('画像2'), upload_to='images',null=True, blank=True)
    image3 = models.ImageField(_('画像3'), upload_to='images',null=True, blank=True)
    name_kanji= models.CharField(_('フルネーム（漢字）'), max_length=32, null=True, blank=True)
    name_kana= models.CharField(_('フルネーム（かな）'), max_length=32, null=True, blank=True)
    birthdate = models.DateTimeField(_('生年月日'), null=True, blank=True)
    gender = models.IntegerField(_('性別'), null=True, blank=True)
    address = models.ForeignKey(LocationModel, verbose_name="住まい（都道府県）", null=True, blank=True, on_delete=models.SET_DEFAULT, default=1,related_name="user_location"  )
    currently_job= models.CharField(_('現在の職業'), max_length=100, null=True, blank=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16)
    education_year = models.IntegerField(_('学歴_年'), null=True, blank=True)
    education_month = models.IntegerField(_('学歴_月'), null=True, blank=True)
    education_status = models.IntegerField(_('学歴_ステータス'), blank=True, default=0)
    school_name = models.CharField(_('学校名'), max_length=32, null=True, blank=True)
    school_type = models.IntegerField(_('学歴_学校種類'), blank=True, default=0)
    school_department = models.CharField(_('学部名'), max_length=32, null=True, blank=True)
    location1 = models.ForeignKey(LocationModel, verbose_name="希望勤務地1", null=True, blank=True, on_delete=models.SET_DEFAULT, default=1, related_name="location1" )
    location2 = models.ForeignKey(LocationModel, verbose_name="希望勤務地2", null=True, blank=True, on_delete=models.SET_DEFAULT, default=1, related_name="location2")
    location3 = models.ForeignKey(LocationModel, verbose_name="希望勤務地3", null=True, blank=True, on_delete=models.SET_DEFAULT, default=1, related_name="location3")
    change_job_time = models.CharField(_('希望入社時期'), max_length=100, null=True, blank=True)
    job_experience1 = models.ForeignKey(SectorModel, verbose_name="経験職種1", null=True, blank=True, on_delete=models.SET_DEFAULT, default=1, related_name="job_experience1"  )
    job_experience2 = models.ForeignKey(SectorModel, verbose_name="経験職種2", null=True, blank=True, on_delete=models.SET_DEFAULT, default=1, related_name="job_experience2"  )
    job_experience3 = models.ForeignKey(SectorModel, verbose_name="経験職種3", null=True, blank=True, on_delete=models.SET_DEFAULT, default=1, related_name="job_experience3"  )
    job_experience_year1 = models.IntegerField(_('経験年数1'), blank=True, default=0)
    job_experience_year2 = models.IntegerField(_('経験年数2'), blank=True, default=0)
    job_experience_year3 = models.IntegerField(_('経験年数3'), blank=True, default=0)


    


    def __str__(self):
        return self.name_kanji
        #return self.last_name + " " + self.first_name

    def is_blank(self):
        if not self.name_kanji:
            return True
        else:
            return False


    class Meta:
        verbose_name = "一般ユーザー"
        verbose_name_plural = "一般ユーザー"
        db_table = "normal_user"
        
        
class CompanyUser(models.Model):
    id = models.CharField(max_length=32, default=ulid.new, primary_key=True, editable=False) 
    company_name = models.CharField(_('法人名称'), max_length=32, blank=True)
    address = models.CharField(_('本社所在地'), max_length=256, blank=True)
    phone_number = models.CharField(_('電話番号'), max_length=16, blank=True)

    def __str__(self):
        return self.company_name

    def is_blank(self):
        if not self.company_name:
            return True
        else:
            return False

    class Meta:
        verbose_name = "企業ユーザー"
        verbose_name_plural = "企業ユーザー"
        db_table = "company_user"
        
    
class User(AbstractBaseUser, PermissionsMixin):
    '''
    カスタムUser
    AbstractBaseUser: 標準のUserモデル
    ※AbstractUserというモデルもあり、これを継承することもできるが、柔軟性が低くなるため非推奨(項目を追加するのみ等の微小なカスタマイズの場合はOK)
    PermissionsMixin: 権限関連のモデル
    '''    
    
    '''
    必須項目
    '''
    id = models.CharField(max_length=32, default=ulid.new, primary_key=True, editable=False) # idは推測されずらく重複しないように、ulidを使用する
    email = models.EmailField(_('メールアドレス'), blank=False, unique=True, db_index=True) 
    username = models.CharField(_('ユーザーネーム'), max_length=150, blank=True)
    user_type = models.IntegerField(_('ユーザータイプ'),  blank=False, default=0)
    normal_user = models.ForeignKey(NormalUser, db_column="normal_user_id" , blank=True, db_index=True, default=None, null=True, on_delete=models.SET_NULL)
    company_user = models.ForeignKey(CompanyUser,  db_column="company_user_id", blank=True, db_index=True, default=None, null=True, on_delete=models.SET_NULL)
    
    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_(
            'Designates whether the user can log into this admin site.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_(
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ),
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    
    # UserManagerを指定
    objects = CustomUserManager()

    '''
    カスタマイズ項目 必要な項目は以下のように追加する
    '''


    
    '''
    フィールド設定
    '''
    # emailの項目名を指定
    EMAIL_FIELD = 'email'
    # ログイン時にIDになる項目名を指定
    USERNAME_FIELD = 'email'
    # 必須入力とする項目名(USERNAME_FIELDに指定した項目は必ず指定する前提のため指定しない)
    REQUIRED_FIELDS = []
    
    
    class Meta:
        '''
        テーブル定義(基本は変更しない)
        '''
        verbose_name = _('ログイン用共通ユーザー')
        verbose_name_plural = _('ログイン用共通ユーザー')
        db_table = "auth_user"

    
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def is_normal_user(self):
        return self.user_type == USER_TYPE.NORMAL_USER
    
    def is_company_user(self):
        return self.user_type == USER_TYPE.COMPANY_USER
    # def get_full_name(self):
    #     return self.last_name + " " + self.first_name


    # def get_short_name(self):
    #     return self.first_name
    

