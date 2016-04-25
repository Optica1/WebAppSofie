from django.conf.urls import patterns, include, url
#from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django_test.forms import ContactForm1, ContactForm2, ContactForm3
from django_test.views import ContactWizard

import settings

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    
    # user auth urls
    url(r'^accounts/login/$',  'django_test.views.login'),
    url(r'^accounts/auth/$',  'django_test.views.auth_view'),    
    url(r'^accounts/logout/$', 'django_test.views.logout'),
    url(r'^accounts/loggedin/$', 'django_test.views.loggedin'),
    url(r'^accounts/invalid/$', 'django_test.views.invalid_login'),
)

if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
   
    urlpatterns += staticfiles_urlpatterns()
