from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=10)
    rollno=models.CharField(max_length=5)
    contact=models.CharField(max_length=10)
    standard=models.IntegerField(max_length=2)
    class Meta:
        db_table="student"