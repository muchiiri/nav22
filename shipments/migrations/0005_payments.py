# Generated by Django 3.2.4 on 2023-01-29 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0004_auto_20221220_1226'),
    ]

    operations = [
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('refno', models.CharField(max_length=100)),
                ('dateexecuted', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('description', models.CharField(max_length=100)),
                ('clearancecosts', models.IntegerField()),
                ('dutybyus', models.IntegerField()),
                ('freightfees', models.IntegerField()),
                ('originfees', models.IntegerField()),
                ('kpademurr', models.IntegerField()),
                ('misc', models.IntegerField()),
                ('terminalhandling', models.IntegerField()),
                ('transportcharges', models.IntegerField()),
                ('agencycharges', models.IntegerField()),
                ('totalcosts', models.IntegerField()),
                ('invoiceno', models.CharField(max_length=100)),
            ],
        ),
    ]