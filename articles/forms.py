from django import forms
from .models import Article

# django form
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content"]

    def clean(self):
        data = self.cleaned_data
        title = data.get("title")
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error("title", f"{title} already in use.")


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()