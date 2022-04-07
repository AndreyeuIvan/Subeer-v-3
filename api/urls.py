from django.contrib import admin
from django.urls import path, include, re_path
from api import views

urlpatterns = [
    re_path("^episode/$", views.EpisodeList.as_view(), name=views.EpisodeList.name),
    re_path(
        "^episode/(?P<pk>[0-9]+)/$",
        views.EpisodeDetail.as_view(),
        name=views.EpisodeDetail.name,
    ),
]
