from django.db import models

class ProjectDepartment(models.Model):

    department = models.ForeignKey("Department", on_delete=models.CASCADE)
    department_hour = models.ForeignKey("DepartmentHour", on_delete=models.CASCADE, null=True)
    project_budget = models.ForeignKey("ProjectBudget", on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()

    class Meta:
            verbose_name = ("ProjectDepartment")
            verbose_name_plural = ("ProjectDepartments")

