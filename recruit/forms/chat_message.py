from django import forms
from ..models import ChatMessageModel


class ChatMessageForm(forms.ModelForm):
    #search_words = forms.CharField(label='検索ワード', required=False)

    class Meta:
        model = ChatMessageModel
        fields = (
            'normal_user',
            'com_user',
            'message',
            'from_user',
        )
