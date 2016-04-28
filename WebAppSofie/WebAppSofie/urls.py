"""WebAppSofie URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.conf.urls import  include, url

# Uncomment the next two lines to enable the admin:

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('viaSofie.urls')),
    # user auth urls
#    url(r'^accounts/login',  'viaSofie.views.login'),
#    url(r'^accounts/auth',  'viaSofie.views.auth_view'),
#    url(r'^accounts/logout', 'viaSofie.views.logout'),
#    url(r'^accounts/loggedin', 'viaSofie.views.loggedin'),
#    url(r'^accounts/invalid', 'viaSofie.views.invalid_login'),
#    url(r'^accounts/register/$', 'viaSofie.views.register_user'),
#    url(r'^accounts/register_success/$', 'viaSofie.views.register_success'),
]
