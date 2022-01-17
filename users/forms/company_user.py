from django.forms import ModelForm, ChoiceField, CharField, Textarea
from users.models import CompanyUser

from app.const import CHOICES

class CompanyUserForm(ModelForm):
    
    address = CharField(
        widget = Textarea,
        required = True,
        max_length = 256,
    )
    
    class Meta:
        model = CompanyUser
        fields = "__all__"