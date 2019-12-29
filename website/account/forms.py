
from django.forms import ModelForm
from .models import Post
class dform(ModelForm):
    class Meta:
        model=Post
        fields=['name','collage','email','rollno','password','male','female']
