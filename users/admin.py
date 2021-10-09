from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from .forms import GroupAdminForm
# Register your models here.

class UserAdminConfig(UserAdmin):
	search_fields = ('email', 'firstname', 'lastname')
	list_filter = ('email', 'firstname', 'lastname','is_active','is_staff')
	ordering = ('-start_date',)
	list_display = ('email','firstname','lastname','is_active','is_staff')

	fieldsets = (
		(None,{'fields':('email', 'firstname', 'lastname','company','address',)}),
		('Permissions',{'fields':('is_staff','is_active')}),

		)

	add_fieldsets = (
		(None,{
			'classes':('wide',),
			'fields':('email','firstname', 'lastname','company','address','password1','password2','is_active','is_staff',)

			}),

		)

admin.site.register(Account,UserAdminConfig)

# Unregister the original Group admin.
admin.site.unregister(Group)

# Create a new Group admin.
class GroupAdmin(admin.ModelAdmin):
    # Use our custom form.
    form = GroupAdminForm
    # Filter permissions horizontal as well.
    filter_horizontal = ['permissions']

# Register the new Group ModelAdmin.
admin.site.register(Group, GroupAdmin)