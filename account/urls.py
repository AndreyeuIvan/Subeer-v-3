from django.contrib import admin
from django.urls import path, include, re_path

from account import views as accounts_views


urlpatterns = [
	re_path(r'^signup/$', accounts_views.signup, name='signup'),
    

]
