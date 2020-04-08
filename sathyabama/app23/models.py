from django.db import models

class StudentModule(models.Model):
    reg=models.IntegerField(unique=True)
    name=models.CharField(max_length=30)
    fname=models.CharField(max_length=30)
    contact=models.IntegerField(unique=True)
    dept=models.CharField(max_length=30)
    email=models.EmailField(max_length=30,unique=True)
    password=models.CharField(max_length=301)