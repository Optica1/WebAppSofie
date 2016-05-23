from django.conf.urls import patterns, include, url
#from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^about$', views.about),
    url(r'^client/(?P<id>\d+)/', views.client),
    url(r'^accounts/login',  views.login),
    url(r'^accounts/auth',  views.auth_view),
    url(r'^accounts/logout', views.logout),
    url(r'^accounts/loggedin', views.loggedin),
    url(r'^accounts/invalid', views.invalid_login),
    url(r'^accounts/register', views.register_user),
    url(r'^accounts/register_success', views.register_success),
    url(r'^sales/properties', views.offer_sales),
    url(r'^sales/property', views.property),
    url(r'^about/sofie', views.about_sofie),
    url(r'^faq', views.faq),
    url(r'^info/privacy', views.privacy),
    url(r'^info/disclaimer', views.disclaimer),
]
