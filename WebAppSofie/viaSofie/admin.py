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

class PropertiesAdmin(admin.ModelAdmin):
    list_display = ['title_dutch']

class UserDetailsInline(admin.StackedInline):
  model = UserDetails
  can_delete = False

class StatusInline(admin.StackedInline):
  model = Status
  can_delete = False

class UserAdmin(UserAdmin):
	inlines = (UserDetailsInline,StatusInline, )

class StatusAdmin(admin.ModelAdmin):
    list_display = ['user']

class PrivacyPageAdmin(admin.ModelAdmin):
    list_display = ['title']

class FaqAdmin(admin.ModelAdmin):
    list_display = ['question']

admin.site.register(Status,StatusAdmin)
admin.site.register(Aboutpage,AboutpageAdmin)
admin.site.register(Properties, PropertiesAdmin)
admin.site.register(PrivacyPage, PrivacyPageAdmin)
admin.site.register(Faq, FaqAdmin)
# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
