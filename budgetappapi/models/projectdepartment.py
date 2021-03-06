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
    def project_length_remaining(self):
        if self.department_hour == None:
            return self.project_budget.length
        else:
            return self.project_budget.length - self.department_hour.month_counter

    @property
    def actual_monthly_cost(self):
        if self.department_hour == None:
            return 0
        else:
            hours_worked = self.department_hour.hours_worked
            dept_cost = hours_worked * self.department.rate
            monthly_cost = dept_cost/self.department_hour.month_counter
            return monthly_cost

    @property
    def actual_project_cost(self):
        if self.department_hour == None:
            return 0
        else:
            return self.actual_monthly_cost * (self.project_length_remaining +1)
            # hours_worked = self.department_hour.hours_worked
            # dept_cost = hours_worked * self.department.rate
            # remaining_cost = self.monthly_cost * self.project_length_remaining
            # return int(dept_cost) + remaining_cost


    @property
    def monthly_dif(self):
        return self.monthly_cost - self.actual_monthly_cost

    @property
    def project_diff(self):
        return self.total_cost - self.actual_project_cost

    @property
    def budgeted_monthly_hours(self):
        quantity = self.department.quantity
        weekly_hours = quantity * 40
        yearly_hours = weekly_hours * 52
        monthly_hours = yearly_hours/12
        return monthly_hours

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


