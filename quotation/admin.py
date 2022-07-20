from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.Quotation)
admin.site.register(models.Quotation_Staff)
admin.site.register(models.Staff_Quotation)
admin.site.register(models.Admin_Quotation)
admin.site.register(models.Quotation_Air)
admin.site.register(models.Quotation_Type)