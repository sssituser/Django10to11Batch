from django.db import models

# Create your models here.
class Employee(models.Model):
    EId = models.IntegerField()
    EName=models.CharField(max_length=30)
    ESal = models.IntegerField()