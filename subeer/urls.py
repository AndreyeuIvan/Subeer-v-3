from django.contrib import admin
from django.urls import path, include, re_path
from .views import SerialList, OpinionList
from subeer import views


urlpatterns = [
    path("", SerialList.as_view(), name="list"),
    path("search", views.search, name="search"),
    path("popular", views.popular, name="popular"),
    path("new_serials", views.new_serials, name="new_serials"),
    path("new_episodes", views.new_episodes, name="new_episodes"),
    path("opinion", views.get_opinion, name="opinion"),
    path("list_opinion", OpinionList.as_view(), name="list_opinion"),
    re_path(r"^like/$", views.serial_like, name="like"),
    path("<slug:slug>/", views.detail_episode, name="details"),
]
