# Generated by Django 3.1.13 on 2022-08-23 20:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0029_auto_20220823_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff_pricing_quotation',
            name='quotation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quote.quote_app'),
        ),
    ]