from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from django.urls import reverse

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
        ("Yes","Yes"),
        ("No","No"),
    )

    user = settings.AUTH_USER_MODEL
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    quote_type = models.CharField(max_length=20)
    incoterm = models.CharField(max_length=30, choices=incoterm_choices, default="EX")
    other_vas = models.CharField(max_length=300, blank=True, null=True)
    county_origin = CountryField(default="US")
    county_destination = CountryField(default="KE")
    cargo_description = models.CharField(max_length=1000, blank=True, null=True)
    goods_category = models.CharField(max_length=30, choices=category, default="No")
    special_delivery = models.CharField(max_length=300, blank=True, null=True)
    quote_serial_no = models.CharField(max_length=30,default="000")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.owner

    # def get_absolute_url(self):
    #     return reverse("quote:list")

class QuoteType(models.Model):
    type_choices = (
        ("Air","Air"),
        ("Sea","Sea"),
        ("Road","Road"),
        ("Warehousing","Warehousing"),
    )
    user = settings.AUTH_USER_MODEL
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=type_choices, default="Air")
    date = models.DateField()
    # quote_serial_no = models.CharField(max_length=30,default="000")

    def __str__(self):
        return self.type

class Quote_Air(Quote):
    # quote_serial_no = models.CharField(max_length=30,default="000")
    cargo_weight = models.FloatField()
    cargo_dimension_length = models.CharField(max_length=100)
    cargo_dimension_width = models.CharField(max_length=100)
    cargo_dimension_height = models.CharField(max_length=100)
    collection_address = models.CharField(max_length=300, blank=True, null=True)

    def save(self, *args, **kwargs):
        Quote_App.objects.create(
            owner = self.owner,
            quote_type=self.quote_type,
            incoterm=self.incoterm,
            country_origin=self.county_origin,
            country_destination=self.county_destination,
            quote_serial_no=self.quote_serial_no,
        )
        super(Quote_Air,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.owner)

class Quote_Sea(Quote):
    # quote_serial_no = models.CharField(max_length=30,default="000")
    container_size = models.FloatField(max_length=100)
    container_dimension_length = models.FloatField()
    container_dimension_width = models.FloatField()
    container_dimension_height = models.FloatField()

    def save(self, *args, **kwargs):
        Quote_App.objects.create(
            owner = self.owner,
            quote_type=self.quote_type,
            incoterm=self.incoterm,
            country_origin=self.county_origin,
            country_destination=self.county_destination,
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
            country_origin=self.county_origin,
            country_destination=self.county_destination,
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
        ("rejected","Rejected"),
    )

    user = settings.AUTH_USER_MODEL
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    quote_type = models.CharField(max_length=200)
    incoterm = models.CharField(max_length=300)
    country_origin = models.CharField(max_length=100)
    country_destination = models.CharField(max_length=100)
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

    quotation = models.ForeignKey(Quote_App,
                            on_delete=models.CASCADE,
                            related_name='quote_app')

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

    buying_port_charges = models.IntegerField(null=True,blank=True)
    selling_port_charges = models.IntegerField(null=True,blank=True)
    margin_port_charges = models.IntegerField(null=True,blank=True)

    buying_other_charges = models.IntegerField(null=True,blank=True)
    selling_other_charges = models.IntegerField(null=True,blank=True)
    margin_other_charges = models.IntegerField(null=True,blank=True)
    
    #freight elements
    buying_freight_cost = models.IntegerField(null=True,blank=True)
    selling_freight_cost = models.IntegerField(null=True,blank=True)
    margin_freight_cost = models.IntegerField(null=True,blank=True)

    buying_other_freight_charges = models.IntegerField(null=True,blank=True)
    selling_other_freight_charges = models.IntegerField(null=True,blank=True)
    margin_other_freight_charges = models.IntegerField(null=True,blank=True)

    buying_total_origin = models.IntegerField(null=True,blank=True)
    selling_total_origin = models.IntegerField(null=True,blank=True)
    margin_total_origin = models.IntegerField(null=True,blank=True)

    #destination charges
    buying_terminal_handling = models.IntegerField(null=True,blank=True)
    selling_terminal_handling = models.IntegerField(null=True,blank=True)
    margin_terminal_handling = models.IntegerField(null=True,blank=True)

    buying_port_charges_dest = models.IntegerField(null=True,blank=True)
    selling_port_charges_dest = models.IntegerField(null=True,blank=True)
    margin_port_charges_dest = models.IntegerField(null=True,blank=True)

    buying_agency_fee = models.IntegerField(null=True,blank=True)
    selling_agency_fee = models.IntegerField(null=True,blank=True)
    margin_agency_fee = models.IntegerField(null=True,blank=True)

    buying_transport_delivery = models.IntegerField(null=True,blank=True)
    selling_transport_delivery = models.IntegerField(null=True,blank=True)
    margin_transport_delivery = models.IntegerField(null=True,blank=True)

    buying_other_destination_charges = models.IntegerField(null=True,blank=True)
    selling_other_destination_charges = models.IntegerField(null=True,blank=True)
    margin_other_destination_charges = models.IntegerField(null=True,blank=True)

    buying_total_destination = models.IntegerField(null=True,blank=True)
    selling_total_destination = models.IntegerField(null=True,blank=True)
    margin_total_destination = models.IntegerField(null=True,blank=True)

    #import duties
    hs_code = models.IntegerField(null=True,blank=True)
    fob_value = models.IntegerField(null=True,blank=True)
    freight_charges = models.IntegerField(null=True,blank=True)
    insurance = models.IntegerField(null=True,blank=True)
    customs_value = models.IntegerField(null=True,blank=True)
    sub_total_duties = models.IntegerField(null=True,blank=True)

    #tax name
    import_duty = models.IntegerField(null=True,blank=True)
    excise_duty = models.IntegerField(null=True,blank=True)
    vat = models.IntegerField(null=True,blank=True)
    railway_levy = models.IntegerField(null=True,blank=True)
    idf_fee = models.IntegerField(null=True,blank=True)
    levies = models.IntegerField(null=True,blank=True)
    sub_total_taxes = models.IntegerField(null=True,blank=True)

    total_tax = models.IntegerField(null=True,blank=True)

    #grand total
    grand_total = models.IntegerField(blank=True)
    status = models.CharField(max_length=20,choices=status_choices,default="pending")