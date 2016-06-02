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

class PlanningInfoInLine(admin.StackedInline):
    model = PlanningInfo
    can_delete =
    extra = 0

class PropertyDocumentsInLine(admin.StackedInline):
    model = PropertyDocuments
    can_delete = False
    extra = 0

class BathroomInLine(admin.StackedInline):
    model = Bathroom
    can_delete = False
    extra = 0

class BedroomInLine(admin.StackedInline):
    model = Bedroom
    can_delete = False
    extra = 0

class GarageInLine(admin.StackedInline):
    model = Garage
    can_delete = False
    extra = 0

class ToiletInLine(admin.StackedInline):
    model = Toilet
    can_delete = False
    extra = 0

class KitchenInLine(admin.StackedInline):
    model = Kitchen
    can_delete = False
    extra = 0

class LivingroomInLine(admin.StackedInline):
    model = Livingroom
    can_delete = False
    extra = 0

class StorageroomInLine(admin.StackedInline):
    model = Storageroom
    can_delete = False
    extra = 0

class PropertyPicturesInLine(admin.StackedInline):
    model = PropertyPictures
    can_delete = False
    extra = 0

class PropertiesAdmin(admin.ModelAdmin):
    list_display = ['title_dutch']
    inlines = (PlanningInfoInLine, PropertyDocumentsInLine, BathroomInLine, BedroomInLine, GarageInLine, ToiletInLine, KitchenInLine, LivingroomInLine, StorageroomInLine, PropertyPicturesInLine)

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

class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name']

class EbookAdmin(admin.ModelAdmin):
    list_display = ['name']

class DisclaimerPageAdmin(admin.ModelAdmin):
    list_display = ['title']

admin.site.register(Status,StatusAdmin)
admin.site.register(Aboutpage,AboutpageAdmin)
admin.site.register(Properties, PropertiesAdmin)
admin.site.register(PrivacyPage, PrivacyPageAdmin)
admin.site.register(Faq, FaqAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(Ebook, EbookAdmin)
admin.site.register(DisclaimerPage, DisclaimerPageAdmin)


# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
