from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
#from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^account', views.account),
    url(r'^accounts/status', views.status),
    url(r'^accounts/login',  views.login),
    url(r'^accounts/auth',  views.auth_view),
    url(r'^accounts/logout', views.logout),
    url(r'^accounts/loggedin', views.loggedin),
    url(r'^accounts/invalid', views.invalid_login),
    url(r'^accounts/register', views.register_user),
    url(r'^accounts/register_success', views.register_success),
    url(r'^sales/forSale', views.offer_sales),
    url(r'^sales/forRent', views.offer_rent),
    url(r'^sales/property/(?P<p_id>[0-9]+)/$', views.property),
    url(r'^about/viaSofie$', views.about),
    url(r'^ebook', views.ebook),
    url(r'^contact', views.contact),
    url(r'^search', views.faqs),    
    url(r'^partner', views.partner),
    url(r'^faq', views.faq),
    url(r'^info/privacy', views.privacy),
    url(r'^info/disclaimer', views.disclaimer),
    url(r'^newsletter/subscribe', views.newsletterSubscribe),
    url(r'^newsletter/unsubscribe', views.newsletterUnsubscribe),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
