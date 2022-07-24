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
        ("CRF","CRF"),
        ("DAP","DAP"),
        ("OTHER","Other"),
    )

    category = (
        ("Yes","Yes"),
        ("No","No"),
    )

    user = settings.AUTH_USER_MODEL
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    incoterm = models.CharField(max_length=30, choices=incoterm_choices, default="EX")
    other_vas = models.CharField(max_length=300, blank=True, null=True)
    county_origin = CountryField(default="US")
    county_destination = CountryField(default="KE")
    cargo_description = models.CharField(max_length=1000, blank=True, null=True)
    goods_category = models.CharField(max_length=30, choices=category, default="No")
    special_delivery = models.CharField(max_length=300, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.owner

    # def get_absolute_url(self):
    #     return reverse("quote:list")

class QuoteType(models.Model):
    type_choices = (
        ("Air","Air"),
        ("Sea","Sea"),
        ("Road","Road"),
        ("Warehouse","Warehouse"),
    )
    user = settings.AUTH_USER_MODEL
    owner = models.ForeignKey(user, on_delete=models.CASCADE)
    type = models.CharField(max_length=30, choices=type_choices, default="Air")
    date = models.DateField()
    def __str__(self):
        return self.type

class Quote_Air(Quote):
    cargo_weight = models.FloatField()
    cargo_dimension_length = models.CharField(max_length=100)
    cargo_dimension_width = models.CharField(max_length=100)
    cargo_dimension_height = models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('quotation:detail', kwargs={'pk': self.pk})

class Quote_Sea(Quote):
    container_size = models.FloatField(max_length=100)
    container_dimension_length = models.FloatField()
    container_dimension_width = models.FloatField()
    container_dimension_height = models.FloatField()

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

class Quote_Warehouse(models.Model):
    cargo_description = models.CharField(max_length=1000)
    cargo_weight = models.FloatField()
    cargo_dimension_length = models.FloatField()
    cargo_dimension_width = models.FloatField()
    cargo_dimension_height = models.FloatField()
    special_delivery = models.CharField(max_length=300, blank=True, null=True)