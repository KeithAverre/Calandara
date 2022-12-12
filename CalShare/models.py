from django.db import models
from django.contrib.auth.models import AbstractUser

from PIL import Image #for image field
from django.core.files import File
from urllib.request import urlopen
from tempfile import NamedTemporaryFile


# User:
#       -Username: Charfield
#       -Email: Charfield (email field if it exists)
#       -Calendars: ManyToMany relationship (a user can have many calendars, a calendar can be owned by many users
#
class User(AbstractUser):
    image = models.ImageField(upload_to='images/profiles', blank=True)


# Category:
#       name: Charfield
#
#
#
class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'
    def __str__(self):
        return self.name




# Calendar:
#       Title: Charfield
#       Category: ManyToMany to Category
#       owner: ManyToMany relationship with User
#       watchers: people who have added to their watching
#       description: textfield
#       image: imageField
#
class Calender(models.Model):
    title = models.CharField(max_length=50)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,default=None, related_name="calendar_owner")
    categories = models.ManyToManyField(Category, blank=True, related_name="calendar_categories")
    watchers = models.ManyToManyField(User, blank=True, related_name="watched_calendars")
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='images/calendars', blank=True)

# Event:
#       Title: Charfield
#       calendar: foreign key to Calendar
#       Start_time: time
#       End_time:   time
#       Start_day: date
#       End_day:  date
class Event(models.Model):
    title = models.CharField(max_length=50)
    calendar = models.ForeignKey(Calender, on_delete=models.CASCADE,related_name="events")
    #datetime https://www.geeksforgeeks.org/datetimefield-django-models/
    start_time = models.DateTimeField()

    end_time = models.DateTimeField()


# Comment:
#       created_at: datetimefield
#       Commenter: foreign key to user
#       calendar: foreign key to calendar
#       comment: textfield
class Comment(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    calendar = models.ForeignKey(Calender, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField(max_length=500)

    def __str__(self):
        return f'{self.comment}'
