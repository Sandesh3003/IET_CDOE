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

class Announcement(models.Model):

    title = models.CharField(max_length=100, blank=False)
    link = models.URLField(blank=False)
    new = models.BooleanField(default=True)

    def __str__(self) :
        return (self.title)

class Notice(models.Model):

    subject = models.CharField(max_length=200, blank=False)
    date = models.DateField(auto_now=True)
    attachement = models.URLField(blank=False)

    def __str__(self) :
        return (self.subject)