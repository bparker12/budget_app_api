from django.db import models
from django.contrib.auth.models import User

class Budgeter(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    class Meta:
            verbose_name = ("Budgeter")
            verbose_name_plural = ("Budgeters")
