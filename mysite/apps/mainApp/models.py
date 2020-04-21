from django.db import models
from django.db.models import CheckConstraint, Q


# Create your models here.

class Devices(models.Model):
    class Meta:
        constraints = [
            CheckConstraint(
                check=~Q(parent_id=None),
                name="parent_id_not_null"),
            models.UniqueConstraint(fields=["name"], name="unique_name")
        ]

    name = models.CharField(max_length=120)
    parent_id = models.IntegerField()

    def __str__(self):
        return self.name
