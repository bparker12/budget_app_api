from django.db import models
from .department import Department
from .departmenthour import DepartmentHour
from .projectbudget import ProjectBudget

class ProjectDepartment(models.Model):

    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    department_hour = models.ForeignKey(DepartmentHour, on_delete=models.CASCADE, null=True)
    project_budget = models.ForeignKey(ProjectBudget, on_delete=models.DO_NOTHING)

    class Meta:
            verbose_name = ("ProjectDepartment")
            verbose_name_plural = ("ProjectDepartments")
