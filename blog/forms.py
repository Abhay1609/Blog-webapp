from django.forms import ModelForm
from .models import Post
class blogform(ModelForm):
    class Meta:
        model= Post
        fields= ['user','title','content','date_posted']

