from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from django.contrib import messages
from django.http import Http404

from .models import User,Event,Calender,Category
from .forms import UserForm, EventForm, CalendarForm

def index(request):
    return render(request, "CalShare/index.html")

def explore(request):
    context = {
        "all_calendars": Calender.objects.all(),
    }
    return render(request, "CalShare/explore.html",context)

def calendar(request, id):
    try:
        cal = Calender.objects.get(pk=id)
    except:
        context = {
            "msg" : f'Calendar {id} not found'
        }
        return render(request,"CalShare/calendar.html",context)
    context={
        "calendar": cal,
        "event_form": EventForm(),
    }
    return render(request,"CalShare/calendar.html",context)

@login_required(login_url="login")
def new_calendar(request):
    if request.method == "POST":
        form = CalendarForm(request.POST, request.FILES)
        if form.is_valid():
            adjusted_form = form.save(commit=False)
            adjusted_form.owner = User.objects.get(username=request.user.username)
            adjusted_form.save()
            form.save_m2m() #required due to not committing it before
            return redirect("calendar", id=adjusted_form.pk)
        else:
            pass
    else:
        pass
    context={
        "calendar_form": CalendarForm(),
    }
    return render(request,"CalShare/new_calendar.html", context)

#search: Calendar: title, description**,
#       Events: name
def search(request):
    term = request.GET["q"]
    all_cal = Calender.objects.all()
    all_events = Event.objects.all()
    context={

    }
    title_s = []
    descr_s = []
    event_s =[]
    if(term != None or term != ""):
        #title search:
        for i in all_cal:

            if(term in i.title):
                title_s.append(i)
                # return redirect("calendar", id=i.pk)
            if(term in i.description):
                descr_s.append(i)
        for f in all_events:
            if (term in f.title):
                event_s.append(f)
        if((len(title_s) + len(descr_s) + len(event_s)) == 0):
            context["msg"] = "No search results found."
        context["title_s"] = title_s
        context["descr_s"] = descr_s
        context["event_s"] = event_s
        return render(request,"CalShare/search.html",context)
        return redirect("explore")
    else:
        return redirect("index")

import random
def random_calendar(request):
    #return render(request, "CalShare/index.html")
    cals = Calender.objects.all()
    k = random.choice(cals)
    return redirect("calendar", id=k.pk)

def my_calendars(request):
    pass


#this is to render contact us page
def contact_us(request):
    return render(request, "CalShare/contact_us.html")

#this handles contacts us form
def contact_us_confirm(request):

    #send email to email if valid email
    return render(request, "CalShare/contact_us_confirm.html")


def change_password(request):
    return render(request, "CalShare/change_password.html")
def change_password_confirm(request):
    if request.method == "POST":
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "CalShare/register.html", {
                "message": "Passwords must match."
            })
    return render(request, "CalShare/change_password_confirm.html")
    pass

from django.http import JsonResponse


def api_event_create(request, parent_cal):
    if request.user.is_authenticated:

        context = {
            "cal_owner": request.user.username,
            "parent_cal": parent_cal,

        }
        print(f'api_event_create called. returning {context}')
        return JsonResponse(context)
    else:
        return JsonResponse({})

def profile(request, id):
    if request.user.is_authenticated and request.user.id == id:
        context = {"user": request.user, "picture": User.objects.get(pk=request.user.id).image, "form":UserForm(instance= User.objects.get(pk=request.user.id))}

        return render(request, "CalShare/profile.html", context)
    else:
        if request.user.is_authenticated:
            return redirect("profile", id=request.user.pk)
        else:
            return redirect("login")

import os
from Calendara.settings import MEDIA_ROOT
def profile_change(request):
    if request.method == "POST":

        form = UserForm(request.POST, request.FILES, instance= User.objects.get(pk=request.user.id))
        if form.is_valid():

            #replace old picture
            if User.objects.get(pk=request.user.id).image != "":
                os.remove(f'{MEDIA_ROOT}\\{User.objects.get(pk=request.user.id).image}')
            form.save()

    return redirect("profile",id=request.user.pk)
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
            # try:
            #     User.objects.get(pk=request.user.id)
            # except:
            #     Profile.objects.create(user=User.objects.get(username=username))
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


