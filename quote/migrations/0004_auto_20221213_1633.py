# Generated by Django 3.2.4 on 2022-12-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_alter_quote_incoterm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote_app',
            name='country_destination',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='quote_app',
            name='country_origin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
