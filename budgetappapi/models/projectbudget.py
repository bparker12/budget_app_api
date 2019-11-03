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

    @property
    def weekly_cost(self):
        projectDepts = ProjectDepartment.objects.filter(project_budget_id=self)
        print(projectDepts)
        # return projectDepts.department.aggregate(total_rate = Sum('rate'))
        # rate = projectDepts.department.aggregate(total_rate = Sum('rate'))

        # return projectDepts.department.rate
        # project_rate = ProjectDepartment.objects.filter(project_budget_id=self).annotate(rate=Sum('') )
        # project_rate = Sum(Case(When(stock__ttype='I', then=F('stock__quantity')), output_field=DecimalField(), default=0)),

        weekly_cost = 0
        length = 0
        rate = 0
        for projectDept in projectDepts:
            departments = Department.objects.filter(id=projectDept.id)
            print(departments)
            rate += departments.rate
            return rate
            # for dept in departments:
            #     rate += dept.rate

            # length += projectDept.department.length
            # weekly_time = projectDept.quantity * 40

            # sum(projectDept.department.rate)
            # weekly_cost = weekly_time * rate
            # return weekly_cost
            # print(rate)

    # @property
    # def monthly_cost(self):
    #     yearly_cost = self.weekly_cost * 52
    #     monthly_cost = yearly_cost/12
    #     return monthly_cost

    # @property
    # def total_cost(self):
    #    return self.monthly_cost * self.length