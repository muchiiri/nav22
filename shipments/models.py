from django.db import models
from django.utils import timezone
from accounts.models import Account

# Create your models here.
class SeaFreightShip(models.Model):
    staff = models.ForeignKey(Account,
                            on_delete=models.CASCADE,
                            related_name='staff_user_sea')
    owner = models.CharField(max_length = 1000)
    refno = models.CharField(max_length = 1000)
    son = models.CharField(max_length = 1000)
    consignee = models.CharField(max_length = 1000)
    billofnumber = models.CharField(max_length=1000)
    customerref = models.CharField(max_length=1000, default='000')
    shippingline = models.CharField(max_length=1000, default='000')
    incoterms = models.CharField(max_length=1000)
    cargo_description = models.CharField(max_length=2000)
    placeofloading = models.CharField(max_length=2000)
    placeofdelivery= models.CharField(max_length=2000)
    containersize = models.CharField(blank=True,max_length=2000)
    unitsize = models.IntegerField()
    unittype = models.CharField(max_length=100)
    current_etd = models.CharField(max_length=100, null=True, blank=True)
    current_eta = models.CharField(max_length=100, null=True, blank=True)
    current_sailingstatus = models.CharField(max_length=100, null=True, blank=True)
    shippingstatus = models.CharField(max_length=100, null=True, blank=True, default='in-progress')


    def __str__(self):
        return self.refno + " - "+ self.owner

class AirFreightShip(models.Model):
    staff = models.ForeignKey(Account,
                            on_delete=models.CASCADE,
                            related_name='staff_user_air')
    owner = models.CharField(max_length = 1000)
    refno = models.CharField(max_length = 1000)
    son = models.CharField(max_length = 1000)
    consignee = models.CharField(max_length = 1000)
    customerref = models.CharField(max_length=1000, default='000')
    shippingline = models.CharField(max_length=1000, default='000')
    billofnumber = models.CharField(max_length=1000)
    incoterms = models.CharField(max_length=1000)
    cargo_description = models.CharField(max_length=2000)
    placeofloading = models.CharField(max_length=2000)
    placeofdelivery= models.CharField(max_length=2000)
    weight = models.CharField(max_length=2000)
    packagesno = models.IntegerField()
    current_etd = models.CharField(max_length=100, null=True, blank=True)
    current_eta = models.CharField(max_length=100, null=True, blank=True)
    current_sailingstatus = models.CharField(max_length=100, null=True, blank=True)
    shippingstatus = models.CharField(max_length=100, null=True, blank=True, default='in-progress')

    def __str__(self):
        return self.refno

class RoadFreightShip(models.Model):
    staff = models.ForeignKey(Account,
                            on_delete=models.CASCADE,
                            related_name='staff_user_road')
    owner = models.CharField(max_length = 1000)
    refno = models.CharField(max_length = 1000)
    son = models.CharField(max_length = 1000)
    consignee = models.CharField(max_length = 1000)
    customerref = models.CharField(max_length=1000, default='000')
    shippingline = models.CharField(max_length=1000, default='000')
    billofnumber = models.CharField(max_length=1000)
    incoterms = models.CharField(max_length=1000)
    cargo_description = models.CharField(max_length=2000)
    placeofloading = models.CharField(max_length=2000)
    placeofdelivery= models.CharField(max_length=2000)
    cargoload = models.CharField(max_length=2000)
    current_etd = models.CharField(max_length=100, null=True, blank=True)
    current_eta = models.CharField(max_length=100, null=True, blank=True)
    current_sailingstatus = models.CharField(max_length=100, null=True, blank=True)
    shippingstatus = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.refno

class FreightForwarding(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    refno = models.CharField(max_length=10000000000000)
    etd = models.CharField(blank=True, null=True, max_length=100)
    eta = models.CharField(blank=True, null=True, max_length=100)
    sailingstatus = models.CharField(max_length=1000)
    update = models.CharField(max_length=1000, blank=True, null=True)
    staffcomments = models.CharField(max_length=1000, blank=True, null=True)
    shippingstatus = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return self.refno

class CustomClearance(models.Model):
    refno = models.CharField(max_length=10000000000000)
    vessel_arrival = models.CharField(max_length=1000)
    entry_transmitted = models.CharField(max_length=1000)
    import_duty_tax = models.CharField(max_length=10)
    exemption_app = models.CharField(max_length=10)
    coc = models.CharField(max_length=100)
    customs_ver = models.CharField(max_length=100)
    kebs_release = models.CharField(max_length=100)
    customs_release= models.CharField(max_length=100)
    loaded_out = models.CharField(max_length=100)
    delivery_client = models.CharField(max_length=100)


