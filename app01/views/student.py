from django.shortcuts import render
from app01 import models

def student(request):
    stu_list = models.Student.objects.all()
    return render(request,'student.html',{'stu_list': stu_list})