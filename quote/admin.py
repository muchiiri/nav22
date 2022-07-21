from django.contrib import admin
from .models import Quote, Quote_Air, Quote_Sea, Quote_Road, Quote_Warehouse
# Register your models here.
admin.site.register(Quote)
admin.site.register(Quote_Air)
admin.site.register(Quote_Sea)
admin.site.register(Quote_Road)
admin.site.register(Quote_Warehouse)