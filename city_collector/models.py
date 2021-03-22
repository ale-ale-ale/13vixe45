from django.db import models


class RandomCity(models.Model):
    city = models.CharField(max_length=30)

    class Meta:
        db_table = 'city'

    def __str__(self):
        return self.city
