from django.forms import ModelForm
from .models import Post,Comment
from django_summernote.widgets import SummernoteWidget

class PostForms(ModelForm):
    class Meta:
        model = Post
        fields = ('title',"desc")
        

class CommentForms(ModelForm):
    class Meta:
        model = Comment
        fields = ("body",)
