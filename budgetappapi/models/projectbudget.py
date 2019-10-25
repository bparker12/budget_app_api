from django.db import models
from .budgeter import Budgeter
from .project_department import ProjectDepartment



class ProductBudget(models.Model):

    budgeter = models.ForeignKey(Budgeter, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    length = models.IntegerField()
    projectDepartment = models.ForeignKey(ProjectDepartment, on_delete=models.CASCADE)

    class Meta:
            verbose_name = ("ProjectBudget")
            verbose_name_plural = ("ProjectBudgets")
