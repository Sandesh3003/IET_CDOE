from django.db import models

class Program(models.Model):
    
    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True)
    eligibility=models.CharField(max_length=200)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    Syllabus=models.TextField(null=True,blank=True)
    Program_objective=models.TextField(null=True,blank=True)
    Course_objective=models.TextField(null=True,blank=True)
    fees=models.CharField(max_length=200)
    apply_now=models.CharField(max_length=200)