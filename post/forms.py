from django import forms
from post.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ("created", "updated", "is_moderated", "views", "url")

    def clean(self):
        print(self.cleaned_data)
        return self.cleaned_data
