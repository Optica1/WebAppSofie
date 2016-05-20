from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# from django.contrib.admin import AdminSite
# from django.utils.translation import ugettext_lazy
from .models import *

class ClientAdmin(admin.ModelAdmin):
    list_display = ['voornaam', 'achternaam']

class AboutpageAdmin(admin.ModelAdmin):
    list_display = ['title']

class UserDetailsInline(admin.StackedInline):
  model = UserDetails
  can_delete = False

class UserAdmin(UserAdmin):
	inlines = (UserDetailsInline, )

# class MyAdminSite(AdminSite):
#     # Text to put at the end of each page's <title>.
#     site_title = ugettext_lazy('My site admin')
#
#     # Text to put in each page's <h1>.
#     site_header = ugettext_lazy('My administration')
#
#     # Text to put at the top of the admin index page.
#     index_title = ugettext_lazy('Site administration')
#
# admin_site = MyAdminSite()

admin.site.register(Aboutpage,AboutpageAdmin)
admin.site.register(Properties)
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
