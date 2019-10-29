from django.db import models
from .budgeter import Budgeter



class ProjectBudget(models.Model):

    budgeter = models.ForeignKey(Budgeter, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    length = models.IntegerField()

    class Meta:
            verbose_name = ("ProjectBudget")
            verbose_name_plural = ("ProjectBudgets")
