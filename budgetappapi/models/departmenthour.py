from django.db import models


class DepartmentHour(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    hours_worked = models.IntegerField()

    class Meta:
            verbose_name = ("Deparment Hours")
            verbose_name_plural = ("Deparment Hours")

