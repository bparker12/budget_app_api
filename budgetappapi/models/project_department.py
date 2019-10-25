from django.db import models
from .department import Department
from .department_hours import DepartmentHours


class ProjectDepartment(models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    department_hours = models.ForeignKey(DepartmentHours, on_delete=models.CASCADE)

    class Meta:
            verbose_name = ("ProjectDepartment")
            verbose_name_plural = ("ProjectDepartments")
