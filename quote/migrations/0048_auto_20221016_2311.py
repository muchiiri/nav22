# Generated by Django 3.1.13 on 2022-10-16 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0047_auto_20221016_2305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='excise_duty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='idf_fee',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='import_duty',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='levies',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='railway_levy',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='total_tax',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='vat',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
