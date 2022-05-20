from django.db import models

class index_content(models.Model):
    #home section
    welcome_header=models.CharField(max_length=200)
    about_head=models.CharField(max_length=200)
    about_body=models.TextField(null=False,blank=False)
    header_image=models.ImageField(null=True ,upload_to='index/')
class footer(models.Model):
    fb_link=models.URLField()
    twitter_link=models.URLField()
    insta_link=models.URLField()
    address=models.TextField()
    contact_num=models.CharField(max_length=12)
    email_id=models.EmailField() 
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

class Faculty(models.Model):

    name = models.CharField(max_length=100, blank=False)
    post = models.CharField(max_length=100, blank=False)
    linked_in = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)

    def __str__(self) :
        return (self.name)

class EmailComingSoon(models.Model):

    email = models.EmailField(max_length=254)

    def __str__(self) :
        return (self.email)