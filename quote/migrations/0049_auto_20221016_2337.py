# Generated by Django 3.1.13 on 2022-10-16 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0048_auto_20221016_2311'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_pricing_quotation',
            name='excise_duty_principal',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='staff_pricing_quotation',
            name='idf_fee_principal',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='staff_pricing_quotation',
            name='import_duty_principal',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='staff_pricing_quotation',
            name='levies_principal',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='staff_pricing_quotation',
            name='railway_levy_principal',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='staff_pricing_quotation',
            name='vat_principal',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
