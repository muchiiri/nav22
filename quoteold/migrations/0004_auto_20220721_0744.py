# Generated by Django 3.1.13 on 2022-07-21 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quote', '0003_quote_road_quote_sea'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote_Warehouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo_description', models.CharField(max_length=1000)),
                ('cargo_weight', models.FloatField()),
                ('cargo_dimension_length', models.FloatField()),
                ('cargo_dimension_width', models.FloatField()),
                ('cargo_dimension_height', models.FloatField()),
                ('special_delivery', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='quote',
            name='special_delivery',
            field=models.CharField(max_length=300),
        ),
    ]
