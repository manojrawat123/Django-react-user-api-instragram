from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="myImg")



class StudentMessges(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to="myImg")
    my_status = models.CharField(max_length=300)