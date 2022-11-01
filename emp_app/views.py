from http.client import HTTPResponse
from django.shortcuts import render, redirect
from .models import *
from .form import *

# Create your views here.
def index(request):
    return render(request, 'emp_app/index.html')

def add_emp(request):
    if request.method=="POST":
        emp_form = empForm(request.POST)
        if emp_form.is_valid:
            emp_form.save()
            return redirect('/')
    
    emp_form=empForm()
    context = {'form': emp_form}
    return render(request, 'emp_app/add_emp.html',context)

def list_emp(request):
    emp = Employee.objects.all()
    context = {'emp':emp,}
    return render(request, 'emp_app/list_emp.html',context)

def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['first_name']
        role = request.POST['role']
        dept = request.POST['dept']
        
        if name:
            emp_list = Employee.objects.filter('first_name'== name)
            return render(request, 'emp_app/list_emp.html',{'emp':emp_list})
    filter_form = filterForm()
    return render(request, 'emp_app/filter_emp.html',{'form':filter_form})

def delete_emp(request, pk=0):
    if pk:
        emp = Employee.objects.get(id=pk)
        emp.delete()
        return HTTPResponse("Employee deleted successfully")
    emp = Employee.objects.all()
    return render(request, 'emp_app/delete_emp.html',{'emps':emp})