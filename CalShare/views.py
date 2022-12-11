from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib import messages
from django.http import Http404

from .models import User


def index(request):
    return render(request, "CalShare/index.html")

def explore(request):
    return render(request, "CalShare/explore.html")

def calendar(request, id):
    pass

#search: Calendar: title, description**,
#       Events: name
def search(request, term):
    pass

def random_calendar(request):
    pass

def my_calendars(request):
    pass


#this is to render contact us page
def contact_us(request):
    return render(request, "CalShare/contact_us.html")

#this handles contacts us form
def contact_us_confirm(request):

    #send email to email if valid email
    return render(request, "CalShare/contact_us_confirm.html")


from django.http import JsonResponse


def api_event_create(request):
    if request.user.is_authenticated:
        pass
    else:
        pass

"""
This is the login section for users
"""
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "CalShare/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "CalShare/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "CalShare/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "CalShare/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "CalShare/register.html")


#This function is to reset a user's password
#   todo: Setup SendGrid
#
#
@login_required(login_url='login')
def change_password(request):
    pass