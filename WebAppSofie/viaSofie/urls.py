from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
#from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from . import views
urlpatterns = i18n_patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^account', views.account, name='account'),
    url(r'^accounts/status', views.status, name='status'),
    url(r'^accounts/login',  views.login, name='login'),
    url(r'^accounts/auth',  views.auth_view, name='auth'),
    url(r'^accounts/logout', views.logout, name='logout'),
    url(r'^accounts/loggedin', views.loggedin, name='loggedin'),
    url(r'^accounts/invalid', views.invalid_login, name='invalid'),
    url(r'^accounts/register', views.register_user, name='register'),
    url(r'^accounts/register_success', views.register_success, name='register success'),
    url(r'^sales/forSale', views.offer_sales, name='sales'),
    url(r'^sales/forRent', views.offer_rent, name='rent'),
    url(r'^sales/property/(?P<p_id>[0-9]+)/$', views.property, name='property'),
    url(r'^about', views.about, name='about'),
    url(r'^ebook', views.ebook, name='ebook'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^partner', views.partner, name='partner'),
    url(r'^faq', views.faq, name='faq'),
    url(r'^info/privacy', views.privacy, name='privacy'),
    url(r'^info/disclaimer', views.disclaimer, name='disclaimer'),
    url(r'^newsletter/subscribe', views.newsletterSubscribe, name='subscribe'),
    url(r'^newsletter/unsubscribe', views.newsletterUnsubscribe, name='unsubscribe'),
)
