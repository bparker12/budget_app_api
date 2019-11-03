from django.db import models
from django.db.models import Sum, Case, When, F
from .budgeter import Budgeter
from .projectdepartment import ProjectDepartment
from .department import Department


class ProjectBudget(models.Model):

    budgeter = models.ForeignKey(Budgeter, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=50)
    length = models.IntegerField()

    class Meta:
            verbose_name = ("ProjectBudget")
            verbose_name_plural = ("ProjectBudgets")

    # @property
    # def department(self):
    #     projectDept = ProjectDepartment.objects.filter(project_budget_id=self)








    @property
    def weekly_cost(self):
        projectDepts = ProjectDepartment.objects.filter(project_budget_id=self)
        print(projectDepts)

        rate = []
        for projectDep in projectDepts:
            print(projectDep.department.rate)
            rate.append(projectDep.department.rate)
            print(rate)
        return sum(rate)


    # @property
    # def monthly_cost(self):
    #     yearly_cost = self.weekly_cost * 52
    #     monthly_cost = yearly_cost/12
    #     return monthly_cost

    # @property
    # def total_cost(self):
    #    return self.monthly_cost * self.length