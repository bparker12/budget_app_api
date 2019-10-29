from django.db import models
from .budgeter import Budgeter

class Department(models.Model):

    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=7, decimal_places=2)
    budgeter = models.ForeignKey(Budgeter, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")