# Generated by Django 3.1.13 on 2022-08-24 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0032_auto_20220824_1008'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_pricing_quotation',
            name='buying_terminal_handling2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staff_pricing_quotation',
            name='margin_terminal_handling2',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='staff_pricing_quotation',
            name='selling_terminal_handling2',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
