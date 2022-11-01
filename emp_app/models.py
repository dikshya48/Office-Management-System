
from django.db import models

# Create your models here.
class Department(models.Model):
    name=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
        
class Role(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
    
class Employee(models.Model):
    first_name=models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    salary=models.FloatField(default=0)
    bonus = models.FloatField(default=0)
    dept=models.ForeignKey(Department, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.first_name+' '+self.last_name
    
    
