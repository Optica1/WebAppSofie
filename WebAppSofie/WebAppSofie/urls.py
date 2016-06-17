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
from django.conf.urls import patterns, include, url
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import javascript_catalog
# from viaSofie.admin import admin_site

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
admin.site.site_header = 'Via Sofie Administratie'

import settings

js_info_dict = {
    'packages': ('viaSofie',),
}

urlpatterns =[

    url(r'^admin', include(admin.site.urls)),
    # url(r'^myadmin', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('viaSofie.urls')),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict),
    url(r'^$', include('viaSofie.urls')),
    # user auth urls
]

urlpatterns += i18n_patterns([url(r'^$', 'viaSofie.views.index', name='home')])


if not settings.DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    urlpatterns += staticfiles_urlpatterns()
