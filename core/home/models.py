from django.db import models

# Create your models here.


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50,null=False,blank=False)
    age = models.IntegerField()
    father_name = models.CharField(max_length=50,null=False,blank=False)
