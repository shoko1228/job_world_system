from django import forms
from ..models import ItemModel, UserFavoriteItemModel


class ItemSearchForm(forms.ModelForm):
    search_words = forms.CharField(label='検索ワード', required=False)
    company_id = forms.CharField(widget=forms.HiddenInput, required=False)

    class Meta:
        model = ItemModel
        fields = (
            'industry',
            'sector',
            'location',
        )
        # widgets = {
        #     'search_words': forms.TextInput(attrs={'class': 'textinputclass'}),
        #     'location_id': forms.Textarea(attrs={'class': 'editable'})
        #     # cssクラスの追加(titleにtextinputclass, textにeditableクラスが追加されるようになる)
        # }

    def filter_items(self, Items):
        """
        入力された検索条件で Items を filter する
        """
        if not self.is_valid():
            return Items

        search_words = self.cleaned_data.get('search_words')
        location = self.cleaned_data.get('location')
        sector = self.cleaned_data.get('sector')
        industry = self.cleaned_data.get('industry')
        company_id = self.cleaned_data.get('company_id')

        if search_words:
            Items = Items.filter(name__contains=search_words)
        if location:
            Items = Items.filter(location=location)
        if industry:
            Items = Items.filter(industry=industry)
        if sector:
            Items = Items.filter(sector=sector)
        if company_id:
            Items = Items.filter(company=company_id)

        return Items