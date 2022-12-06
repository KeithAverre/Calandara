from django.contrib import admin
from .models import User, Calender, Event, Profile, Comment, Category

admin.site.register(User)
admin.site.register(Calender)
admin.site.register(Event)
admin.site.register(Profile)
admin.site.register(Comment)
admin.site.register(Category)