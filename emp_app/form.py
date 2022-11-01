from django.forms import ModelForm
from .models import *

class empForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class filterForm(ModelForm):
    class Meta:
        model=Employee
        fields = ['first_name','dept','role']