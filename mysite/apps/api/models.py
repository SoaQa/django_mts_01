from django.db import models
from django.contrib.postgres.fields import JSONField


# Create your models here.
from django.db.models import CheckConstraint, Q


class Vendor(models.Model):
    class Meta:
        db_table = "vendors"
        constraints = [
            models.UniqueConstraint(fields=["name"], name="unique_vendor_name")
        ]

    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name


    def __repr__(self):
        return 'sas'


class Device(models.Model):
    class Meta:
        db_table = "devices"
        constraints = [
            CheckConstraint(
                check=~Q(name=None),
                name="name_not_null"),
            models.UniqueConstraint(fields=["name"], name="unique_device_name")
        ]
    name = models.CharField(max_length=120)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class FirmwareVersion(models.Model):
    class Meta:
        db_table = "firmware_versions"
        constraints = [
            CheckConstraint(
                check=~Q(version=None), name="version_not_null"
            ),
            models.UniqueConstraint(fields=["version"], name="unique_version")
        ]
    version = models.CharField(max_length=120)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)

    def __str__(self):
        return self.version


class Firmware(models.Model):
    class Meta:
        db_table = "firmwares"
        constraints = [
            CheckConstraint(
                check=~Q(data=None), name="data_not_null"
            ),
        ]
    version = models.ForeignKey(FirmwareVersion, on_delete=models.CASCADE)
    data = JSONField(name="data")
