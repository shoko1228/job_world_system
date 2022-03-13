from django.forms import ModelForm, ChoiceField, CharField, Textarea,DateField,SelectDateWidget
from users.models import NormalUser
from django.contrib.admin.widgets import AdminDateWidget

from app.const import CHOICES

class NormalUserForm(ModelForm):
    
    gender = ChoiceField(
        choices = CHOICES.GENDER
    )

    status = ChoiceField(
        choices = CHOICES.STATUS
    )

    address = CharField(
        widget = Textarea,
        required = True,
        max_length = 256,
    )
    
    class Meta:
        model = NormalUser
        fields = "__all__"
        widgets = {
            'birthdate': SelectDateWidget
        }


