# Generated by Django 3.2.4 on 2023-02-05 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shipments', '0008_auto_20230201_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payments',
            old_name='agencycharges',
            new_name='paymentamount',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='clearancecosts',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='dutybyus',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='freightfees',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='kpademurr',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='misc',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='originfees',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='terminalhandling',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='totalcosts',
        ),
        migrations.RemoveField(
            model_name='payments',
            name='transportcharges',
        ),
        migrations.AddField(
            model_name='payments',
            name='paymenttype',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='payments',
            name='shippingline',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
