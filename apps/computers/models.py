from django.db import models


class ComputerModel(models.Model):
    class Meta:
        db_table = 'computers'

    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    ram = models.IntegerField()
    diagonal = models.IntegerField()
