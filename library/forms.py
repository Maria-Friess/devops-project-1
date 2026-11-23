from django import forms

from library.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["name", "link", "annotation", "status"]
