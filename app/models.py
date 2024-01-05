from django.db import models

# Create your models here.
class Employee(models.Model):
   Empname=models.CharField(max_length=100)
   Empid=models.IntegerField()
   
   def __str__(self):
       return self.Empname
    
    
class Emp(models.Model):
    Empname=models.OneToOneField(Employee,on_delete=models.CASCADE)
    Empname=models.CharField(max_length=100)
    Empid=models.IntegerField()
    
    
    def __str__(self):
        return self.Empname