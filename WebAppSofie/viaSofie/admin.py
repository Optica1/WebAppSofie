from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
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

admin.site.register(Aboutpage,AboutpageAdmin)
admin.site.register(Properties)
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
