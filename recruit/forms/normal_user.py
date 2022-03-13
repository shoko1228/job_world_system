from django import forms
from ..models import ItemModel, UserFavoriteItemModel
from users.models import NormalUser


class NormalUserSearchForm(forms.ModelForm):
    search_words = forms.CharField(label='検索ワード', required=False)

    class Meta:
        model = NormalUser
        fields = (
            'location'
        )
        # widgets = {
        #     'search_words': forms.TextInput(attrs={'class': 'textinputclass'}),
        #     'location_id': forms.Textarea(attrs={'class': 'editable'})
        #     # cssクラスの追加(titleにtextinputclass, textにeditableクラスが追加されるようになる)
        # }

    def filter_items(self, NormalUsers):
        """
        入力された検索条件で Items を filter する
        """
        if not self.is_valid():
            return NormalUsers

        search_words = self.cleaned_data.get('search_words')
        location = self.cleaned_data.get('location')
        sector = self.cleaned_data.get('sector')
        industry = self.cleaned_data.get('industry')
        if search_words:
            NormalUsers = NormalUsers.filter(name__contains=search_words)
        if location:
            NormalUsers = NormalUsers.filter(location=location)
        if industry:
            NormalUsers = NormalUsers.filter(industry=industry)
        if sector:
            NormalUsers = NormalUsers.filter(sector=sector)
        return NormalUsers