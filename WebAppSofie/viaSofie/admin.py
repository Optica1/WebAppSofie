from django.contrib import admin

from viaSofie.models import UserDetails

class UserDetailsInline(admin.StackedInline):
  model = UserDetails
  can_delete = False

class UserAdmin(UserAdmin):
	inlines = (UserDetailsInline)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)