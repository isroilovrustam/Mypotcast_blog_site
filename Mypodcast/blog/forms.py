from django import forms
from .models import CommentArticle, CommentBlog


class CommentArticleForm(forms.ModelForm):
    class Meta:
        model = CommentArticle
        fields = '__all__'
        exclude = ['article', 'author']

    def __init__(self, *args, **kwargs):
        super(CommentArticleForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name


class CommentBlogForm(forms.ModelForm):
    class Meta:
        model = CommentBlog
        fields = '__all__'
        exclude = ['article', 'author']

    def __init__(self, *args, **kwargs):
        super(CommentBlogForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field_name