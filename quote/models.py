from email.policy import default
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from django.urls import reverse
# import all from accounts
from accounts.models import *

# Create your models here.
class Quote(models.Model):
    #incoterms
    incoterm_choices = (
        ("EX","EX Works"),
        ("FOB","FOB"),
        ("CFR","CFR"),
        ("DAP","DAP"),
        ("OTHER","Other"),
    )

    category = (
        ("","------"),
        ("Dangerous","Dangerous"),
        ("Non-Dangerous","Non-Dangerous"),
    )

    user = settings.AUTH_USER_MODEL
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    quote_type = models.CharField(max_length=20)
    incoterm = models.CharField(max_length=30, choices=incoterm_choices, default="EX")
    other_vas = models.CharField(max_length=300, blank=True, null=True)
    Country_of_Origin = CountryField(default="US")
    Country_of_Destination = CountryField(default="KE")
    cargo_description = models.CharField(max_length=1000, blank=True, null=True)
    Nature_of_Cargo = models.CharField(max_length=30, choices=category, default="No")
    special_delivery = models.CharField(max_length=300, blank=True, null=True)
    quote_serial_no = models.CharField(max_length=30,default="000")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class QuoteType(models.Model):
    type_choices = (
        ("Air","Air"),
        ("Sea","Sea"),
        ("Road","Road"),
        ("Warehouse","Warehouse"),
    )
    user = settings.AUTH_USER_MODEL
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    #owner= models.CharField(max_length=50, choices=[(account.email,account) for account in Account.objects.filter(is_staff="False")])
    type = models.CharField(max_length=30, choices=type_choices, default="Air")
    date = models.DateField()
    # quote_serial_no = models.CharField(max_length=30,default="000")

    def __str__(self):
        return self.type

class Quote_Air(Quote):
    # quote_serial_no = models.CharField(max_length=30,default="000")
    cargo_weight = models.FloatField()
    Volume_CBM = models.CharField(max_length=100)
    # cargo_dimension_length = models.CharField(max_length=100)
    # cargo_dimension_width = models.CharField(max_length=100)
    # cargo_dimension_height = models.CharField(max_length=100)
    collection_address = models.CharField(max_length=300, blank=True, null=True)

    def save(self, *args, **kwargs):
        Quote_App.objects.create(
            owner = self.owner,
            quote_type=self.quote_type,
            incoterm=self.incoterm,
            country_origin=self.Country_of_Origin,
            country_destination=self.Country_of_Destination,
            quote_serial_no=self.quote_serial_no,
        )
        super(Quote_Air,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.owner)

class Quote_Sea(Quote):
    container_choices = (
        ("","-------"),
        ("1x20FT","1x20FT"),
        ("1x40FT","1x40FT"),
        ("1x40HC","1x40HC"),
        ("1x40 Reefer","1x40 Reefer")
    )
    
    # quote_serial_no = models.CharField(max_length=30,default="000")
    container_size = models.CharField(max_length=100, choices=container_choices, default="No")
    Gross_Weight = models.FloatField()
    # container_dimension_length = models.FloatField()
    # container_dimension_width = models.FloatField()
    # container_dimension_height = models.FloatField()

    def save(self, *args, **kwargs):
        Quote_App.objects.create(
            owner = self.owner,
            quote_type=self.quote_type,
            incoterm=self.incoterm,
            country_origin=self.Country_of_Origin,
            country_destination=self.Country_of_Destination,
            quote_serial_no=self.quote_serial_no,
        )
        super(Quote_Sea,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.owner)

class Quote_Road(Quote):
    truck_choices  = (
        ("Van","Van"),
        ("3T Truck","3T Truck"),
        ("5T Truck","5T Truck"),
        ("7T Truck","7T Truck"),
        ("15T Truck","15T Truck"),
        ("28T Truck","28T Truck"),
    )
    
    truck_type = models.CharField(max_length=30, choices=truck_choices)
    cargo_weight = models.FloatField()
    cargo_dimension_length = models.FloatField()
    cargo_dimension_width = models.FloatField()
    cargo_dimension_height = models.FloatField()
    collection_address = models.CharField(max_length=300, blank=True, null=True)
    delivery_address = models.CharField(max_length=300, blank=True, null=True)

    def save(self, *args, **kwargs):
        Quote_App.objects.create(
            owner = self.owner,
            quote_type=self.quote_type,
            incoterm=self.incoterm,
            # country_origin=self.Country_of_Origin,
            # country_destination=self.Country_of_Destination,
            quote_serial_no=self.quote_serial_no,
        )
        super(Quote_Road,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.owner)

class Quote_Warehouse(models.Model):
    user = settings.AUTH_USER_MODEL
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    cargo_description = models.CharField(max_length=1000)
    cargo_weight = models.FloatField()
    cargo_dimension_length = models.FloatField()
    cargo_dimension_width = models.FloatField()
    cargo_dimension_height = models.FloatField()
    special_delivery = models.CharField(max_length=300, blank=True, null=True)
    quote_serial_no = models.CharField(max_length=30,default="000")

    def save(self, *args, **kwargs):
        Quote_App.objects.create(
            owner = self.owner,
            quote_type=self.quote_type,
            incoterm="Warehouse",
            country_origin="KE",
            country_destination="KE",
            quote_serial_no=self.quote_serial_no,
        )
        super(Quote_Warehouse,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.owner)


class Quote_App(models.Model):
    status_choices = (
        ("pending","Pending"),
        ("review","Review"),
        ("approved_admin","Approved_Admin"),
        ("approved_client","Approved_Client"),
        ("rejected_client","Rejected_Client"),
        ("rejected","Rejected"),
    )

    user = settings.AUTH_USER_MODEL
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    quote_type = models.CharField(max_length=200)
    incoterm = models.CharField(max_length=300)
    country_origin = models.CharField(max_length=100, null=True, blank=True)
    country_destination = models.CharField(max_length=100, null=True, blank=True)
    quote_serial_no = models.CharField(max_length=30,default="000")
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=30, choices=status_choices, default="pending")

    def __str__(self):
        return str(self.owner)

class Staff_Pricing_Quotation(models.Model):
    status_choices = (
        ("pending","Pending"),
        ("review","Review"),
        ("approved","Approved"),
        ("rejected","Rejected"),
    )

    quotation = models.ForeignKey(Quote_App, on_delete=models.CASCADE)
    agent_name = models.CharField(max_length=1000)
    
    #origin charges
    buying_origin_haulage = models.IntegerField(null=True,blank=True)
    selling_origin_haulage = models.IntegerField(null=True,blank=True)
    margin_origin_haulage = models.IntegerField(null=True,blank=True)

    buying_customs_documentation = models.IntegerField(null=True,blank=True)
    selling_customs_documentation = models.IntegerField(null=True,blank=True)
    margin_customs_documentation = models.IntegerField(null=True,blank=True)

    buying_origin_terminal_handling = models.IntegerField(null=True,blank=True)
    selling_origin_terminal_handling = models.IntegerField(null=True,blank=True)
    margin_origin_terminal_handling = models.IntegerField(null=True,blank=True)

    buying_airport_charges = models.IntegerField(null=True,blank=True)
    selling_airport_charges = models.IntegerField(null=True,blank=True)
    margin_airport_charges = models.IntegerField(null=True,blank=True)

    buying_other_charges_A = models.IntegerField(null=True,blank=True)
    selling_other_charges_A = models.IntegerField(null=True,blank=True)
    margin_other_charges_A = models.IntegerField(null=True,blank=True)
    
    #totals of section A
    buying_total_A = models.IntegerField(null=True,blank=True,default=0)
    selling_total_A = models.IntegerField(null=True,blank=True,default=0)
    margin_total_A = models.IntegerField(null=True,blank=True,default=0)

    #freight elements
    buying_freight_cost = models.IntegerField(null=True,blank=True)
    selling_freight_cost = models.IntegerField(null=True,blank=True)
    margin_freight_cost = models.IntegerField(null=True,blank=True)

    buying_other_freight_charges = models.IntegerField(null=True,blank=True)
    selling_other_freight_charges = models.IntegerField(null=True,blank=True)
    margin_other_freight_charges = models.IntegerField(null=True,blank=True)
    
    #totals of section B
    buying_total_B = models.IntegerField(null=True,blank=True,default=0)
    selling_total_B = models.IntegerField(null=True,blank=True,default=0)
    margin_total_B = models.IntegerField(null=True,blank=True,default=0)

    buying_terminal_handling = models.IntegerField(null=True,blank=True)
    selling_terminal_handling = models.IntegerField(null=True,blank=True)
    margin_terminal_handling = models.IntegerField(null=True,blank=True)

    
    buying_agency_fee = models.IntegerField(null=True,blank=True)
    selling_agency_fee = models.IntegerField(null=True,blank=True)
    margin_agency_fee = models.IntegerField(null=True,blank=True)

    buying_transport_delivery = models.IntegerField(null=True,blank=True)
    selling_transport_delivery = models.IntegerField(null=True,blank=True)
    margin_transport_delivery = models.IntegerField(null=True,blank=True)

    buying_other_destination_charges = models.IntegerField(null=True,blank=True)
    selling_other_destination_charges = models.IntegerField(null=True,blank=True)
    margin_other_destination_charges = models.IntegerField(null=True,blank=True)

    #totals of section C
    buying_total_C = models.IntegerField(null=True,blank=True,default=0)
    selling_total_C = models.IntegerField(null=True,blank=True,default=0)
    margin_total_C = models.IntegerField(null=True,blank=True,default=0)

    #import duties
    hs_code_bp = models.CharField(null=True,max_length=100,blank=True)
    hs_code_sp = models.IntegerField(null=True,blank=True)
    hs_code_margin = models.IntegerField(null=True,blank=True)

    fob_value_bp = models.CharField(null=True,max_length=100,blank=True)
    fob_value_sp = models.IntegerField(null=True,blank=True)
    fob_value_margin = models.IntegerField(null=True,blank=True)

    freight_charges_bp = models.IntegerField(null=True,blank=True)
    freight_charges_sp = models.IntegerField(null=True,blank=True)
    freight_charges_margin = models.IntegerField(null=True,blank=True)

    insurance_bp = models.IntegerField(null=True,blank=True)
    insurance_sp = models.IntegerField(null=True,blank=True)
    insurance_margin = models.IntegerField(null=True,blank=True)

    customs_value_bp = models.IntegerField(null=True,blank=True)
    customs_value_sp = models.IntegerField(null=True,blank=True)
    customs_value_margin = models.IntegerField(null=True,blank=True)

    #total D
    buying_total_D = models.IntegerField(null=True,blank=True,default=0)
    selling_total_D = models.IntegerField(null=True,blank=True,default=0)
    margin_total_D = models.IntegerField(null=True,blank=True,default=0)

    #tax name
    import_duty_principal = models.CharField(max_length=1000,null=True,blank=True)
    import_duty = models.IntegerField(null=True,blank=True,default=0)

    excise_duty_principal = models.CharField(max_length=1000,null=True,blank=True)
    excise_duty = models.IntegerField(null=True,blank=True,default=0)

    vat_principal = models.CharField(max_length=1000,null=True,blank=True)
    vat = models.IntegerField(null=True,blank=True,default=0)

    railway_levy_principal = models.CharField(max_length=1000,null=True,blank=True)
    railway_levy = models.IntegerField(null=True,blank=True,default=0)

    idf_fee_principal = models.CharField(max_length=1000,null=True,blank=True)
    idf_fee = models.IntegerField(null=True,blank=True,default=0)

    levies_principal = models.CharField(max_length=1000,null=True,blank=True)
    levies = models.IntegerField(null=True,blank=True,default=0)
    total_tax = models.IntegerField(null=True,blank=True,default=0)

    #grand total
    grand_total_bp = models.IntegerField(null=True,blank=True,default=0)
    grand_total_sp = models.IntegerField(null=True,blank=True,default=0)
    grand_total_margin = models.IntegerField(null=True,blank=True,default=0)
    status = models.CharField(max_length=20,choices=status_choices,default="pending")

    def __str__(self):
        return str(self.agent_name)
    
    #save total taxes
    def save(self,*args,**kwargs):
        self.total_tax = int(self.import_duty) + int(self.excise_duty) + int(self.vat) + int(self.railway_levy) + int(self.idf_fee) + int(self.levies)
        super().save(*args,**kwargs)

class Taxes(models.Model):
    name = models.CharField(max_length=1000)
    percentage = models.IntegerField(default=0)
    amount = models.IntegerField(null=True,blank=True)
    value = models.IntegerField(null=True,blank=True,default=0)

    def __str__(self):
        return str(self.name)

    def save(self,*args,**kwargs):
        self.value = int(self.amount) * int(self.percentage) / 100
        super(Taxes,self).save(*args,**kwargs)