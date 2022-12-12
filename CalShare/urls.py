from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("change_password", views.change_password, name="change_password"),


    path("explore", views.explore, name="explore"),
    path("calendar/<int:id>/", views.calendar, name="calendar"),
    path("new_calendar", views.new_calendar, name="new_calendar"),
    path("my_calendars", views.my_calendars, name="my_calendars"),

    path("search", views.search, name="search"),
    path("random_calendar/", views.random_calendar, name="random_calendar"),

    path("contact_us", views.contact_us, name="contact_us"),
    path("contact_us_confirm", views.contact_us_confirm, name="contact_us_confirm"),
    path("change_password", views.change_password, name="change_password"),
    path("change_password_confirm", views.change_password_confirm, name="change_password_confirm"),

    path("api_event_create/<int:parent_cal>", views.api_event_create, name = "api_event_create"),
    path("profile/<int:id>", views.profile, name="profile"),
    path("profile_change", views.profile_change, name="profile_change"),
]