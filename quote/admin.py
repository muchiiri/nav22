from django.contrib import admin
from .models import Quote, Quote_Air, Quote_Sea, Quote_Road, Quote_Warehouse, QuoteType, Quote_App,Staff_Pricing_Quotation,Taxes

# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id','owner','created_at','updated_at')
    list_filter = ('created_at','owner')
    search_fields = ('id','owner','created_at','updated_at')
    ordering = ('-created_at',)

class Quote_AirAdmin(admin.ModelAdmin):
    list_display = ('id','quote_type','quote_serial_no', 'owner', 'incoterm', 'collection_address', 'cargo_weight') 
    list_display_links =('id', 'quote_serial_no', 'quote_type', 'owner')
    list_filter = ('quote_serial_no', 'owner')

class Quote_SeaAdmin(admin.ModelAdmin):
    list_display = ('id','quote_type','quote_serial_no', 'owner', 'incoterm', 'container_size') 
    list_display_links =('id', 'quote_serial_no', 'quote_type', 'owner')
    list_filter = ('quote_serial_no', 'owner')

class Quote_RoadAdmin(admin.ModelAdmin):
    list_display = ('id','quote_type','quote_serial_no', 'owner', 'incoterm') 
    list_display_links =('id', 'quote_serial_no', 'quote_type', 'owner')
    list_filter = ('quote_serial_no', 'owner')


class Quote_WarehouseAdmin(admin.ModelAdmin):
    list_display = ('id','quote_serial_no', 'owner') 
    list_display_links =('id', 'quote_serial_no','owner')
    list_filter = ('quote_serial_no', 'owner')

class Quote_AppAdmin(admin.ModelAdmin):
    list_display = ('id', 'quote_serial_no','quote_type', 'owner', 'status')
    list_display_links = ('id', 'quote_serial_no','quote_type' )
    list_filter = ('quote_serial_no','quote_type', 'owner')

admin.site.register(Quote,QuoteAdmin)
admin.site.register(Quote_Air,Quote_AirAdmin)
admin.site.register(Quote_Sea,Quote_SeaAdmin)
admin.site.register(Quote_Road,Quote_RoadAdmin)
admin.site.register(Quote_Warehouse,Quote_WarehouseAdmin)
admin.site.register(QuoteType)
admin.site.register(Quote_App, Quote_AppAdmin)
admin.site.register(Staff_Pricing_Quotation)
admin.site.register(Taxes)