# Generated by Django 3.1.13 on 2022-11-02 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0050_auto_20221102_2110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='fob_value_bp',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
