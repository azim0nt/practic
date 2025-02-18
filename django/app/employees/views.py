from django.shortcuts import render, redirect
from .models import Employees
from .forms import EmployeesForm



def employees(request):
    employees_data = Employees.objects.all()

    return render(request,'employees.html', context={'employees':employees_data})


def new_employee(request):
    if request.method == 'POST':
        form = EmployeesForm(request.POST)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            return redirect('employees')
    else:
        form = EmployeesForm()
    return render(request, 'new_employee.html', context={'form':form})