# Generated by Django 3.1.13 on 2022-10-04 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0043_auto_20220929_0104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote_app',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('review', 'Review'), ('approved_admin', 'Approved_Admin'), ('approved_client', 'Approved_Client'), ('rejected_client', 'Rejected_Client'), ('rejected', 'Rejected')], default='pending', max_length=30),
        ),
    ]
