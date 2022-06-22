from math import degrees
from os import terminal_size
from django.db import models
from accounts.models import Account
# Create your models here.

class Quotation(models.Model):
    #type of freight
    FreightType = (
    ("air","Air Freight"),
    ("sea","Sea Freight"),
    ("road","Road Freight"),
    ("warehouse","Ware Housing"),
    )

    #cargoload
    CargoLoad = (
        ("full","Full Container(FCL)"),
        ("less","Less Than Container Load(LCL)"),
        ("conventional","Conventional Cargo/Bulk"),
    )

    #incoterms
    Incoterms = (
        ("EX","EX Works"),
        ("FOB","FOB"),
        ("CRF","CRF"),
        ("DAP","DAP"),
        ("OTHER","Other"),
    )

    category = (
        ("yes","Yes"),
        ("no","No"),
    )

    status_choices = (
        ("pending","Pending"),
        ("review","Review"),
        ("approved_admin","Approved_Admin"),
        ("approved_client","Approved_Client"),
        ("rejected","Rejected"),
    )

    owner = models.CharField(max_length = 1000,default="anonymous")
    staff_owner = models.CharField(max_length=1000,default="anonymous")
    quote_number = models.CharField(max_length=10000,default="00000")
    date = models.CharField(max_length=1000,blank=True)
    # updated_at = models.DateTimeField(auto_now=True)

    type = models.CharField(max_length=20,choices=FreightType,default="sea")
    cargoload = models.CharField(max_length=20,choices=CargoLoad,default="full")
    incoterms = models.CharField(max_length=20,choices=Incoterms,default="EX")
    container_size = models.CharField(max_length=20)
    cargo_length = models.CharField(max_length=20)
    cargo_width = models.CharField(max_length=20)
    cargo_height = models.CharField(max_length=20)
    country_origin = models.CharField(max_length=100)
    collection_address = models.CharField(max_length=500)
    cargo_description = models.CharField(max_length=500)
    goods_category = models.CharField(max_length=20,choices=category,default="no")
    special_instructions = models.CharField(max_length=1000)
    status = models.CharField(max_length=20,choices=status_choices,default="pending")


class Quotation_Staff(models.Model):
    staff = models.ForeignKey(Account,
                            on_delete=models.CASCADE,
                            related_name='staff_owner_quote')

    quotations = models.IntegerField()

    def __str__(self):
        return str(self.staff) + "=" + str(self.quotations)

class Staff_Quotation(models.Model):
    status_choices = (
        ("pending","Pending"),
        ("review","Review"),
        ("approved","Approved"),
        ("rejected","Rejected"),
    )

    quotation = models.ForeignKey(Quotation,
                            on_delete=models.CASCADE,
                            related_name='quote')

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

class Admin_Quotation(models.Model):
    status_choices = (
        ("approved","Approved"),
        ("ammend","Ammend"),
        ("rejected","Rejected"),
    )

    quotation = models.ForeignKey(Quotation,
                            on_delete=models.CASCADE,
                            related_name='quote_admin')

    status_admin  = models.CharField(max_length=20,choices=status_choices)
    comment = models.CharField(max_length=1000,null=True,blank=True)