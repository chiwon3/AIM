from django.forms import ModelForm
from .models import Blog

class BlogForms(ModelForm):
    class Meta : 
        model = Blog
        fields = ('title','nick','desc','contact',)