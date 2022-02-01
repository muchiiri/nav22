from django import forms
from shipments.models import *
from accounts.models import *

STATUS_CHOICES = [
    ('in-progress', 'In Progress'),
    ('completed', 'Completed'),
    ]

INCOTERMS_CHOICES= [
        ('exw', 'EXW'),
    ('fca', 'FCA'),
    ('fas', 'FAS'),
    ('fob', 'FOB'),
    ('cpt', 'CPT'),
    ('cfr', 'CFR'),
    ('cif', 'CIF'),
    ('cip', 'CIP'),
    ('dat', 'DAT'),
    ('dap', 'DAP'),
    ('ddp', 'DDP'),
    ]

CARGOLOAD_CHOICES= [
    ('kilograms', "(KG) Kilogram(s)"),
    ('tonnes', "(T)Tonne(s)"),
]

CONTAINER_CHOICES= [
    ('20 FT', "20 FT"),
    ('40 FT', "40 FT"),
]

SHIPPING_CHOICES= [
    ('maersk', "MAERSK"),
    ('cmacgm', "CMA CGM"),
    ('esl', "ESL"),
    ('pil', "PIL"),
    ('cosco', "COSCO"),
    ('hpl', "HPL"),
    ('zim', "ZIM"),
    ('one', "ONE"),
    ('msc', "MSC"),
    ('emc', "EMC"),
]

AIRLINE_CHOICES= [
    ('ET', "ET"),
    ('EMIRATES', "EMIRATES"),
    ('QATAR', "QATAR"),
    ('KQ', "KQ"),
    ('KLM', "KLM"),
    ('RWANDAAIR', "RWANDA AIR"),
    ('SINGAPORE', "SINGAPORE"),
    ('BRITISH', "BRITISH"),
    ('TURKISH', "TURKISH"),
    ('RAFTANZA', "RAFTANZA"),
    ('ETIHAD', "ETIHAD"),
    ('ASTRAL', "ASTRAL"),
    ('CHINASOUTHERN', "CHINA SOUTHERN"),
    ('SOUTHAFRICANAIRLINE', "SOUTHAFRICAN AIRLINE"),
    ('EGYPTAIR', "EGYPT AIR"),
    ('VIRGINAIR', "VIRGIN AIR"),
    ('MALAWIANAIR', "MALAWIAN AIR"),
]

class RoadFreightShipForm(forms.ModelForm):
    # owner=forms.ChoiceField(choices=[(account.email,account) for account in Account.objects.filter(is_staff="False")])
    refno = forms.CharField(widget=forms.TextInput({"readonly":"True"}))
    incoterms =  forms.CharField(widget=forms.Select(choices=INCOTERMS_CHOICES))
    cargoload = forms.CharField(widget=forms.Select(choices=CARGOLOAD_CHOICES))
    shippingline = forms.CharField(widget=forms.Select(choices=SHIPPING_CHOICES))
    shippingstatus = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES),required=False)
    # containersize = forms.CharField(widget=forms.Select(choices=CONTAINER_CHOICES))
    class Meta:
        model = RoadFreightShip
        exclude = ('staff',)
        #fields = '__all__'
        labels = {
            'refno':'Reference Number',
            'son':'Shipping Order No',
            'consignee':'Consignee',
            'billofnumber':'Bill of Lading',
            'cargo_description':'Cargo Description',
            'placeofloading':'Place of Loading',
            'placeofdelivery':'Place of Delivery',
            'customerref':'Customer Ref#',
        }

        # widgets = {
        #     'owner':forms.ChoiceField(choices=Account.objects.all())
        # }

class AirFreightShipForm(forms.ModelForm):
    # owner=forms.ChoiceField(choices=[(account.email,account) for account in Account.objects.filter(is_staff="False")])
    refno = forms.CharField(widget=forms.TextInput({"readonly":"True"}))
    incoterms = forms.CharField(widget=forms.Select(choices=INCOTERMS_CHOICES))
    shippingline = forms.CharField(widget=forms.Select(choices=AIRLINE_CHOICES))
    cargoload = forms.CharField(widget=forms.Select(choices=CARGOLOAD_CHOICES))
    # shippingstatus = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES))
    # containersize = forms.CharField(widget=forms.Select(choices=CONTAINER_CHOICES))
    class Meta:
        model = AirFreightShip
        exclude = ('staff',)

        labels = {
            'refno':'Reference Number',
            'son':'Shipping Order No',
            'consignee':'Consignee',
            'billofnumber':'Bill of Lading',
            'cargo_description':'Cargo Description',
            'placeofloading':'Place of Loading',
            'placeofdelivery':'Place of Delivery',
            'customerref':'Customer Ref#',
        }

class SeaFreightShipForm(forms.ModelForm):
    # owner=forms.ChoiceField(choices=[(account.email,account) for account in Account.objects.filter(is_staff="False")])
    refno = forms.CharField(widget=forms.TextInput({"readonly":"True"}))
    incoterms = forms.CharField(widget=forms.Select(choices=INCOTERMS_CHOICES))
    shippingline = forms.CharField(widget=forms.Select(choices=SHIPPING_CHOICES))
    cargoload = forms.CharField(widget=forms.Select(choices=CARGOLOAD_CHOICES))
    containersize = forms.CharField(widget=forms.Select(choices=CONTAINER_CHOICES))
    shippingstatus = forms.CharField(widget=forms.Select(choices=STATUS_CHOICES),required=False)
    class Meta:
        model = SeaFreightShip
        exclude = ('staff',)

        labels = {
            'refno':'Reference Number',
            'son':'Shipping Order No',
            'consignee':'Consignee',
            'billofnumber':'Bill of Lading',
            'cargo_description':'Cargo Description',
            'placeofloading':'Place of Loading',
            'placeofdelivery':'Place of Delivery',
            'customerref':'Customer Ref#',
        }

