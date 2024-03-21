from django.db import models

# Create your models here.
class StudentData(models.Model):
    sname=models.CharField(max_length=20)
    sage=models.IntegerField()
    smobile=models.IntegerField()
