from django import forms
from .models import User, Calender, Event

class EventForm(forms.ModelForm):

    class Meta:
        model = Event
        fields = ('title','start_time', 'end_time',"start_day","end_day")
        widgets={
            "start_time": forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            "end_time": forms.TimeInput(format='%H:%M',attrs={'type': 'time'}),
            "start_day": forms.DateInput(attrs={'type': 'date'}),
            "end_day":forms.DateInput(attrs={'type': 'date'}),
        }

class UserForm(forms.ModelForm):

    class Meta:
        model = User
        #fields = ('categories', 'image', 'image_url', 'title', 'description', 'bid')
        fields = ('username','email', 'image')

class CalendarForm(forms.ModelForm):
    class Meta:
        model = Calender
        fields = ("title", "categories", "description", "image")