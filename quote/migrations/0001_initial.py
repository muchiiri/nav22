# Generated by Django 3.1.13 on 2022-07-21 10:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('incoterm', models.CharField(choices=[('EX', 'EX Works'), ('FOB', 'FOB'), ('CRF', 'CRF'), ('DAP', 'DAP'), ('OTHER', 'Other')], default='EX', max_length=30)),
                ('county_origin', django_countries.fields.CountryField(default='US', max_length=2)),
                ('county_destination', django_countries.fields.CountryField(default='KE', max_length=2)),
                ('cargo_description', models.CharField(max_length=1000)),
                ('goods_category', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=30)),
                ('special_delivery', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='No', max_length=30)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]