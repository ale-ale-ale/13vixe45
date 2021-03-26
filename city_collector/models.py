from django.contrib.postgres.fields import JSONField
from django.db import models


class SomeCity(models.Model):
    city = JSONField()

    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.city
