from distutils.command import upload
from email.mime import image
from email.policy import default
from pkgutil import ImpLoader
from random import choices
from re import T, template
from statistics import mode
from unicodedata import category
from django.db import models
from django.conf import settings
from django.core.mail import EmailMultiAlternatives, send_mail
from django.forms import CharField, EmailField, IntegerField
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 

class Slide(models.Model):
    image = models.ImageField(upload_to='images/slides/')

class UsefulLink(models.Model):
    name=models.CharField(max_length=200,null=True)
    display_image=models.ImageField(upload_to='images/useful_links/')
    goto_link=models.URLField(blank=True)
    def __str__(self):
        return(self.name)

class Index(models.Model):
    #home section
    announcements_on_load = models.BooleanField(default=False)
    logo=models.ImageField(upload_to='images/index/',default='images/index/cdoe1.png')
    slides = models.ManyToManyField(Slide)
    welcome_header=models.CharField(max_length=200)
    welcome_header_highlighted=models.CharField(max_length=200, default=' ')
    slider_text=models.CharField(max_length=200)
    about_head=models.CharField(max_length=200)
    about_body=models.TextField(null=False,blank=False)
    header_image=models.ImageField(null=True ,upload_to='images/index/')
    mission_head=models.CharField(max_length=200,default="Mission");
    mission_text=models.TextField(default=" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. ")
    vission_head=models.CharField(max_length=200,default='Vision');
    vission_text=models.TextField(default=" Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. ")
    num_of_online_courses=models.IntegerField(validators=[MinValueValidator(0)],default=0, blank=True, null=True)
    num_of_dl_courses=models.IntegerField(validators=[MinValueValidator(0)],default=0, blank=True, null=True)
    num_of_faculties=models.IntegerField(validators=[MinValueValidator(0)],default=0, blank=True, null=True)
    num_of_students=models.IntegerField(validators=[MinValueValidator(0)],default=0, blank=True, null=True)
    useful_link=models.ManyToManyField(UsefulLink)
    fb_link=models.URLField(default='#', blank=True)
    twitter_link=models.URLField(default='#', blank=True)
    insta_link=models.URLField(default='#', blank=True)
    address=models.TextField(null=True, blank=True)
    map_link=models.URLField(max_length=200, null=True, blank=True)
    contact_num=models.CharField(max_length=12, null=True,blank=True)
    email_id=models.EmailField(null=True,blank=True)
    website=models.URLField(default='#', null=True ,blank=True)


    def __str__():
        return("Index") 

class Faculty(models.Model):

    name = models.CharField(max_length=100, blank=False)
    post = models.CharField(max_length=100, blank=False)
    linked_in = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    faculty_image=models.ImageField(upload_to='images/faculty/',default='images/faculty/team.png')
    def __str__(self) :
        return (self.name)

class Team(models.Model):
    name = models.CharField(max_length=100, blank=False)
    post = models.CharField(max_length=100, blank=False)
    linked_in = models.URLField(blank=True)
    github = models.URLField(blank=True)
    instagram = models.URLField(blank=True)
    team_image=models.ImageField(upload_to='images/team/',default='images/team/team.png')
    def __str__(self) :
        return (self.name)

class Program(models.Model):
    program_id=models.CharField(max_length=100)
    program_name=models.CharField(primary_key='True',max_length=200)
    def __str__(self):
        return (self.program_name) 

class CourseType(models.Model):
    type_id=models.CharField(max_length=100)
    course_type=models.CharField(primary_key='True',max_length=200)
    def __str__(self):
        return (self.course_type) 

class CourseDetail(models.Model):
    CATEGIRY_CHOICES = (
    ('General Degree','General Degree'),
    ('Professional Degree', 'Professional Degree'),
    )
    course_id=models.CharField(primary_key='True',max_length=100,default='001')
    program_name=models.ForeignKey(Program,on_delete=models.CASCADE,default='offline')
    course_name=models.CharField(max_length=200,default=" enter course name")
    specialization=models.CharField(max_length=200,default=" ", null=True, blank=True)
    category=models.CharField(max_length=20, choices=CATEGIRY_CHOICES, default='General Degree')
    card_image=models.ImageField(upload_to='images/course_image/',null=True)
    course_type=models.ForeignKey(CourseType,on_delete=models.CASCADE,default='undergrad')
    faculty=models.ForeignKey(Faculty,on_delete=models.CASCADE)
    display_title=models.CharField(max_length=200)
    # display_image=models.ImageField(upload_to='images/course_image/display_images/')
    apply_link=models.URLField(default='#')
    course_summary=models.TextField(max_length=400,default="Lorem ipsum gravida nibh vel velit auctor aliquetn sollicitudirem quibibendum auci elit cons equat ipsutis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris. Morbi accumsan ipsum velit. Nam nec tellus .")
    course_prerequisites=models.TextField(max_length=400,default="Lorem ipsum gravida nibh vel velit auctor aliquetn sollicitudirem quibibendum auci elit cons equat ipsutis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris. Morbi accumsan ipsum velit. Nam nec tellus .")
    course_eligibility=models.TextField(max_length=400,default="Lorem ipsum gravida nibh vel velit auctor aliquetn sollicitudirem quibibendum auci elit cons equat ipsutis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris. Morbi accumsan ipsum velit. Nam nec tellus .")
    course_syllabus=models.FileField(upload_to="pdf/syllabus/",null=True ,default='pdf/syllabus.pdf')
    course_fee_structure=models.FileField(upload_to="pdf/fee/",null=True ,default='pdf/fee structure.pdf')
    course_duration=models.CharField(max_length=100, default="x-y months", blank="False")
    academic_calendar=models.FileField(upload_to="pdf/academicCalendar/", null=True, default='pdf/academicCalendar.pdf')
    admission_process=models.TextField(max_length=400,default="Lorem ipsum gravida nibh vel velit auctor aliquetn sollicitudirem quibibendum auci elit cons equat ipsutis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris. Morbi accumsan ipsum velit. Nam nec tellus .")
    documents_required=models.TextField(max_length=400,default="Lorem ipsum gravida nibh vel velit auctor aliquetn sollicitudirem quibibendum auci elit cons equat ipsutis sem nibh id elit. Duis sed odio sit amet nibh vulputate cursus a sit amet mauris. Morbi accumsan ipsum velit. Nam nec tellus .")

    def __str__(self):
        return (self.course_name+'('+self.specialization+')')
    
class Compliance(models.Model):
    ugc_2f=models.FileField(upload_to="pdf/ugc_2f/", null=True, default='pdf/ugc.pdf')
    ugc_12B=models.FileField(upload_to="pdf/ugc_12B/", null=True, default="pdf/ugc.pdf")
    naac=models.FileField(upload_to="pdf/naac/", null=True, default="pdf/ugc.pdf")
    deb_ugc=models.FileField(upload_to="pdf/deb_ugc/", null=True, default="pdf/ugc.pdf")
    aicte=models.FileField(upload_to="pdf/aicte/", null=True, default="pdf/ugc.pdf")
    ciqa=models.FileField(upload_to="pdf/ciqa/", null=True, default="pdf/ugc.pdf")

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

# class Review(models.Model):
    
#     review_id=models.AutoField(primary_key='True')
#     course_name=models.ForeignKey(course_head,on_delete=models.CASCADE,default='Introduction To Data Science')
#     reviewer_name=models.CharField(max_length=200,default="anonymus")
#     reviewer_image=models.ImageField(upload_to="images/review/",default='images/review/team.png')
#     date=models.DateField(auto_now_add='True')
#     rating=models.IntegerField(choices=[(0,0),(1,1),(2,2),(3,3),(4,4),(5,5)],validators=[MinValueValidator(1), MaxValueValidator(5)])
#     review=models.TextField(max_length=200)

#     def __str__(self):
#         return (self.reviewer_name)
    

class ComingSoonMailList(models.Model):

    email = models.EmailField(max_length=254)

    def __str__(self):
        return self.email

class Newsletter(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    subject = models.CharField(max_length=150)
    template = models.FileField(upload_to='uploaded_newsletters/')

    def __str__(self):
        return self.subject + " " + self.created_at.strftime("%B %d, %Y")
    
    def send(self, request):
        # contents = str(self.template.read().decode('utf-8'))
        subscribers = ComingSoonMailList.objects.all()
        response_email = render_to_string(self.template.name)
        for sub in subscribers:
            mail = EmailMultiAlternatives(self.subject, response_email, settings.EMAIL_HOST_USER, [sub.email])
            mail.content_subtype = 'html'
            mail.send()