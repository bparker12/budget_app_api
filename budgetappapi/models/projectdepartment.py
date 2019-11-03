from django.db import models
class ProjectDepartment(models.Model):

    department = models.ForeignKey("Department", on_delete=models.DO_NOTHING)
    department_hour = models.ForeignKey("DepartmentHour", on_delete=models.CASCADE, null=True)
    project_budget = models.ForeignKey("ProjectBudget", on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(null=True)

    class Meta:
            verbose_name = ("ProjectDepartment")
            verbose_name_plural = ("ProjectDepartments")

    @property
    def weekly_cost(self):
        rate = self.department.rate
        quantity = self.department.quantity

        weekly_time = quantity * 40
        weekly_cost = weekly_time * rate
        return weekly_cost

    @property
    def monthly_cost(self):
        yearly_cost = self.weekly_cost * 52
        monthly_cost = yearly_cost/12
        return monthly_cost

    @property
    def total_cost(self):
        length = self.project_budget.length
        total_cost = self.monthly_cost * length
        return total_cost

