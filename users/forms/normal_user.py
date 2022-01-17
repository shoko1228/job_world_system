from django.forms import ModelForm, ChoiceField, CharField, Textarea
from users.models import NormalUser

from app.const import CHOICES

class NormalUserForm(ModelForm):
    
    gender = ChoiceField(
        choices = CHOICES.GENDER
    )
    
    address = CharField(
        widget = Textarea,
        required = True,
        max_length = 256,
    )
    
    class Meta:
        model = NormalUser
        fields = "__all__"