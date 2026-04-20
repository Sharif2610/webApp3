from django.db import models

# Create your models here.
class Employees(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    hire_date = models.DateField()
    salary = models.DecimalField(max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name