from django.conf.urls import  include, url
#from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from . import views


urlpatterns =[

    # user auth urls
    url(r'^$', views.index),
    url(r'^accounts/login/$',  views.login , name="login"),
    url(r'^accounts/auth/$',  views.auth_view, name="auth"),
    url(r'^accounts/logout/$', views.logout, name="logout"),
    url(r'^accounts/loggedin/$', views.loggedin, name="loggedin"),
    url(r'^accounts/invalid/$', views.invalid_login , name="invalid")
]
