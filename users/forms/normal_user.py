from django.forms import ModelForm, ChoiceField, CharField, Textarea,DateField,SelectDateWidget
from users.models import NormalUser
from django.contrib.admin.widgets import AdminDateWidget

import datetime

from app.const import CHOICES

class NormalUserForm(ModelForm):
    
    gender = ChoiceField(
        choices = CHOICES.GENDER
    )

    status = ChoiceField(
        choices = CHOICES.STATUS
    )

    education_status = ChoiceField(
        choices = CHOICES.EDUCATION_STATUS
    )  

    education_year = ChoiceField(
        choices = CHOICES.YEARS
    )  

    education_month = ChoiceField(
        choices = CHOICES.MONTHS
    )  

    school_type = ChoiceField(
        choices = CHOICES.SCHOOL_TYPE
    )  

    job_experience_year1 = ChoiceField(
        choices = CHOICES.NUMBERS
    )  

    job_experience_year2 = ChoiceField(
        choices = CHOICES.NUMBERS
    )

    job_experience_year3 = ChoiceField(
        choices = CHOICES.NUMBERS
    )    

    # address = CharField(
    #     widget = Textarea,
    #     #required = True,
    #     max_length = 256,
    # )
    
    class Meta:
        model = NormalUser
        fields = "__all__"
        today = datetime.date.today()
        widgets = {
            'birthdate': SelectDateWidget(years=[x for x in range(1950, today.year)])
        }

