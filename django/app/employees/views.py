from django.shortcuts import render
from .models import Employees


def employees(request):
    employees_data = Employees.objects.all()

    return render(request,'employees.html', context={'employees':employees_data})
