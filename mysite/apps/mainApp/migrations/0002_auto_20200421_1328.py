# Generated by Django 3.0.4 on 2020-04-21 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='device',
            table='devices',
        ),
        migrations.AlterModelTable(
            name='firmwareversion',
            table='firmware_versions',
        ),
        migrations.AlterModelTable(
            name='vendor',
            table='vendors',
        ),
    ]
