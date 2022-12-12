from django import forms
from .models import User, Calender, Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title','start_time', 'end_time')

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        #fields = ('categories', 'image', 'image_url', 'title', 'description', 'bid')
        fields = ('username','email', 'image')

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calender
        fields = ("title", "categories", "description", "image")