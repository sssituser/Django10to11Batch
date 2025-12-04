from django.db import models

# Create your models here.
class Product(models.Model):
    productId=models.IntegerField()
    name=models.CharField(max_length=30)
    price =models.IntegerField()
    quan = models.IntegerField()

