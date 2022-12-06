from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


# User:
#       -Username: Charfield
#       -Email: Charfield (email field if it exists)
#       -Calendars: ManyToMany relationship (a user can have many calendars, a calendar can be owned by many users
#
class User(AbstractUser):

    pass

# Profile:
#       -profile img (add picture functionality
#       -User: foreign key to User. 1-1
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="profile_user")
    pass


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


# Event:
#       Title: Charfield
#       Start_time: time (maybe)
#       End_time:   time
#       Start_day: date
#       End_day:  date
class Event(models.Model):
    pass

# Calendar:
#       Title: Charfield
#       Category: ManyToMany to Category
#       Admin: Foreign key relationship with User
#       Events: foreign key. 1-M
#
#
#
class Calender(models.Model):
    title = models.CharField(max_length=50)
    categories = models.ManyToManyField(Category, blank=True, related_name="calendars")
    pass

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
