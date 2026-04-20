from django.db import models

# Create your models here.
class Department(models.Model):
    deptno = models.IntegerField(primary_key=True)
    deptname = models.CharField(max_length=50)

class Workforce(models.Model):
    wfno = models.IntegerField(primary_key=True)
    wfname = models.CharField(max_length=50)
    salary = models.FloatField()
    department = models.ForeignKey(Department,on_delete=models.CASCADE)

    def __str__(self):
        return self.wfname