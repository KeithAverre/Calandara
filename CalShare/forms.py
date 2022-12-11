from django import forms
from .models import User, Calender


# Create your forms here.
class UserForm(forms.ModelForm):

    class Meta:
        model = User
        #fields = ('categories', 'image', 'image_url', 'title', 'description', 'bid')
        fields = ('username','email', 'image')