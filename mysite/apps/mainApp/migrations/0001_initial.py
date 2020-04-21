# Generated by Django 3.0.4 on 2020-04-21 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='FirmwareVersion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=120)),
            ],
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
            ],
        ),
        migrations.AddConstraint(
            model_name='vendor',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_vendor_name'),
        ),
        migrations.AddField(
            model_name='firmwareversion',
            name='device_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Device'),
        ),
        migrations.AddField(
            model_name='device',
            name='vendor_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Vendor'),
        ),
        migrations.AddConstraint(
            model_name='firmwareversion',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, version=None), name='version_not_null'),
        ),
        migrations.AddConstraint(
            model_name='firmwareversion',
            constraint=models.UniqueConstraint(fields=('version',), name='unique_version'),
        ),
        migrations.AddConstraint(
            model_name='device',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, name=None), name='name_not_null'),
        ),
        migrations.AddConstraint(
            model_name='device',
            constraint=models.UniqueConstraint(fields=('name',), name='unique_device_name'),
        ),
    ]
