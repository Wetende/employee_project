from django.shortcuts import render
from .forms import EmployeeForms

# Create your views here.

def employee_list(request):
    return render(request, "employee_register/employee_list.html")

def employee_form(request):
    form = EmployeeForms()
    return render(request, "employee_register/employee_form.html",{'form':form})

def employee_delete(request):
    return