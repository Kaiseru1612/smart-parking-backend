# Generated by Django 3.2.15 on 2022-11-02 08:36

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('parking_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parkinglot',
            name='area',
            field=django.contrib.gis.db.models.fields.PolygonField(default=((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0, 0.0)), srid=4326),
        ),
    ]