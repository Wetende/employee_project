from django.shortcuts import render, redirect
from .forms import EmployeeForms
from .models import Employee

# Create your views here.

def employee_list(request):
    context = {'employee_list':Employee.objects.all()}
    return render(request, "employee_register/employee_list.html",context)

def employee_form(request):
    if request.method == "GET":
      form =  EmployeeForms
   
      return render(request, "employee_register/employee_form.html",{'form':form})

    else: 
        form = EmployeeForms(request.POST)
    if form.is_valid():
          form.save()
    return redirect('/employee/list')

def employee_delete(request):
    return