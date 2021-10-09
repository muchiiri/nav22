from django.contrib import admin
from .models import *
#from django.contrib.auth.admin import UserAdmin
# Register your models here.

# @admin.register(RoadFreightShip)
class RoadFreightConfig(admin.ModelAdmin):
	# search_fields = ('staff', 'owner', 'refno')
	list_filter = ('staff', 'owner', 'refno')
	ordering = ('refno',)
	list_display = ('owner', 'staff', 'refno')

	# fieldsets = (
	# 	(None,{'fields':('staff', 'owner', 'refno',)}),

	# 	)

	# add_fieldsets = (
	# 	(None,{
	# 		'classes':('wide',),
	# 		'fields':('staff',)

	# 		}),

	# 	)
class AirFreightConfig(admin.ModelAdmin):
	# search_fields = ('staff', 'owner', 'refno')
	list_filter = ('staff', 'owner', 'refno')
	ordering = ('refno',)
	list_display = ('owner', 'staff', 'refno')

class SeaFreightConfig(admin.ModelAdmin):
	# search_fields = ('staff', 'owner', 'refno')
	list_filter = ('staff', 'owner', 'refno')
	ordering = ('refno',)
	list_display = ('owner', 'staff', 'refno')

class FreightForwardConfig(admin.ModelAdmin):
	# search_fields = ('staff', 'owner', 'refno')
	list_filter = ('refno','etd', 'etd')
	ordering = ('refno',)
	list_display = ('refno','etd', 'etd')

admin.site.register(RoadFreightShip,RoadFreightConfig)
admin.site.register(AirFreightShip,AirFreightConfig)
admin.site.register(SeaFreightShip,SeaFreightConfig)
admin.site.register(FreightForwarding,FreightForwardConfig)