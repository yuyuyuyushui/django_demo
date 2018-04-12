from django.shortcuts import render,HttpResponse
from app01 import models
def student(request):
    stu_list = models.Student.objects.all()
    cls_list = models.Classes.objects.all()
    for row in stu_list:
        print(row.username)
    return render(request, 'student.html', {'stu_list': stu_list,'cls_list':cls_list})

def add_student(request):
    u = request.POST.get('username')
    a = request.POST.get('age')
    g = request.POST.get('gender')
    c = request.POST.get('cls_id')

    models.Student.objects.create(
            username=u,
            age = a,
            gender= g,
            cls_id = c
                            )
    return HttpResponse('200')