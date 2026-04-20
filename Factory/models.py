from django.db import models

# Create your models here.
class Factory(models.Model):
    name = models.CharField(max_length=50)
    role = models.CharField(max_length=50)
    salary = models.IntegerField()
    location = models.CharField(max_length=50)
    ph_no = models.BigIntegerField()

    def __str__(self):
        return self.name