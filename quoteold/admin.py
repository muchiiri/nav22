from django.contrib import admin
from .models import Quote, Quote_Air, Quote_Sea, Quote_Road, Quote_Warehouse, QuoteType, Quote_App,Staff_Pricing_Quotation


# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id','owner','created_at','updated_at')
    list_filter = ('created_at','owner')
    # search_fields = ('id','owner','created_at','updated_at')
    ordering = ('-created_at',)

admin.site.register(Quote,QuoteAdmin)
admin.site.register(Quote_Air)
admin.site.register(Quote_Sea)
admin.site.register(Quote_Road)
admin.site.register(Quote_Warehouse)
admin.site.register(QuoteType)
admin.site.register(Quote_App)
admin.site.register(Staff_Pricing_Quotation)