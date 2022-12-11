from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("change_password", views.change_password, name="change_password"),


    path("explore", views.explore, name="explore"),
    path("calendar/<str:TITLE>/", views.calendar, name="calendar"),
    path("my_calendars", views.my_calendars, name="my_calendars"),

    path("search/<str:term>", views.search, name="search"),
    path("random_calendar/", views.random_calendar, name="random_calendar"),

    path("contact_us", views.contact_us, name="contact_us"),
    path("contact_us_confrim", views.contact_us_confrim, name="contact_us_confrim"),
]