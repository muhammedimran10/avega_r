from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    phno = models.CharField(max_length=10)
    clg_name = models.CharField(max_length=30)
    corse_name = models.CharField(max_length=10)