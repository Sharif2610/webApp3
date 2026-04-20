from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Clients(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    salary = models.IntegerField()

    def __str__(self):
        return self.name