from django.db import models

# Create your models here.


class Classes(models.Model):
    title = models.CharField(max_length=32)
    m = models.ManyToManyField('Teacher')


class Teacher(models.Model):
    name = models.CharField(max_length=32)

class Student(models.Model):

    username = models.CharField(max_length=32)
    age = models.IntegerField()
    gender = models.CharField(max_length=32)
    cs = models.ForeignKey('Classes',on_delete=False)