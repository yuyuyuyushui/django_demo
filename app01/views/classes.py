from django.shortcuts import render
from app01 import models

def get_classes(request):
    cls_list = models.Classes.objects.all()
    return render(request, 'get_classes.html', {'cls_list': cls_list})