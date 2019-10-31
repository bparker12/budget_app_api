from django.db import models
from .budgeter import Budgeter
from .projectdepartment import ProjectDepartment

class Department(models.Model):

    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    rate = models.DecimalField(max_digits=7, decimal_places=2)
    budgeter = models.ForeignKey(Budgeter, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = ("Department")
        verbose_name_plural = ("Departments")

    @property
    def employees_left(self):
        employees = ProjectDepartment.objects.filter(department=self)
        remaining = 0
        for employee in employees:
            remaining = self.quantity - employee.quantity
            return remaining