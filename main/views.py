from contextlib import nullcontext
import email
import imp
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import *
import random
from main import forms



# Create your views here.
# def prog(request,pk):
#     program=Program.objects.get(id=pk) 
#     context={'program':program}
#     return render(request,"main\course_page.html")


def index(request):
    
    index=Index.objects.filter()[:1].get()
    announcement=Announcement.objects.all()
    programs=Programs.objects.all()
    context={'announcements': announcement,'index':index,'programs':programs, 'faculty': Faculty.objects.all(),}
    return render(request, 'index.html',context)

def comingsoon(request):
    index=Index.objects.filter()[:1].get()
    programs=Programs.objects.all()
    context={'form': forms.ComingsoonForm(),'index':index,'programs':programs}
    if request.method == 'POST':
        emailid = request.POST['email']
        validate=ComingSoonMailList.objects.filter(email=emailid).all()
        if(len(validate)!=0):
            context['status']= 'Email ID already exist'
            return render(request, 'coming_soon.html',context)
        else:
            sub = ComingSoonMailList(email=emailid)
            sub.save()
            context['status']= 'Email ID added'
            return render(request, 'coming_soon.html',context)
    else:
        return render(request, 'coming_soon.html', context) 

def faculty(request):
    index=Index.objects.filter()[:1].get()
    programs=Programs.objects.all()
    context={'faculty': Faculty.objects.all(),'index':index,'programs':programs}
    return render(request, 'faculty.html', context)

def team(request):
    index=Index.objects.filter()[:1].get()
    programs=Programs.objects.all()
    context={'team': Team.objects.all(),'index':index,'programs':programs}
    return render(request, 'teams_s.html', context)

def programs(request,pk):
    index=Index.objects.filter()[:1].get()
    programs=Programs.objects.all()
    context={'index':index,'programs':programs}
    subheads=course_type.objects.all()
    courses=course_head.objects.filter(program_name=pk).all()
    
    subhead_active = subheads[0]
    subheads = subheads[1:]

    context={'index':index,'programs':programs,
            'courses':courses,'subheads':subheads, 
            'subhead_active': subhead_active,
            'program_name': pk}
    if(len(courses)==0):
        return comingsoon(request) 
    else:
        return render(request, 'courses.html', context)
    
         


def notices(request):
    notice=Notice.objects.all()
    index=Index.objects.filter()[:1].get()
    programs=Programs.objects.all()
    return render(request, 'notices.html', {'notices': notice, 'index': index, 'programs':programs})

def course(request,pk,ic):
    if request.method == 'POST':
        if 'first_name' in request.POST:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            mobile_number = request.POST.get('mobile_number')
            emailid = request.POST.get('emailid')
            qualification = request.POST.get('qualification')
            c_nm=course_head.objects.filter(course_name=ic).filter(program_name__program_name=pk).get()
            sub = Student(first_name=first_name, last_name=last_name, mobile_number=mobile_number, emailid=emailid, qualification=qualification, course_enrolling_for = c_nm)
            sub.save()
           
        # else:
        #     name = request.POST.get('name')
        #     rates = request.POST.get('rating')
        #     rev = request.POST.get('review')
        #     c_nm=course_head.objects.filter(course_name=ic).filter(program_name__program_name=pk).get()
            
        #     sub = Review.objects.create(reviewer_name=name, rating=rates, review=rev, course_name = c_nm)
        #     sub.save()
    index=Index.objects.filter()[:1].get()
    programs=Programs.objects.all()
    rating=Review.objects.filter(course_name__program_name=pk).filter(course_name__course_name=ic).values('rating').all()
    reviews=Review.objects.filter(course_name__program_name=pk).filter(course_name__course_name=ic).all()
    
    val=dict()
    for rate in range(len(rating)):
        if rating[rate]['rating'] in val.keys():
            val[rating[rate]['rating']]=val[rating[rate]['rating']]+1
        else:
            val[rating[rate]['rating']]=1
    maxi=0
    if(len(rating)!=0):
        maxi=0
        fcount=0
        for x in val.keys():
             if(val[x]>fcount):
                 fcount=val[x]
                 maxi=x

        num_of_reviews=len(rating)
    else:
        num_of_reviews="NO"
    over_rate=range(maxi)
    negative=range(5-maxi)
    course_det=course_details.objects.filter(course_name__course_name=ic).filter(course_name__program_name=pk).get()
    context={'index':index,'programs':programs,'course_detail':course_det,'overall_rating':over_rate,'negative':negative,'num_of_reviews':num_of_reviews,'reviews':reviews}
    
    
    
    return render(request, 'course.html', context)

def temp(request):
    index=Index.objects.filter()[:1].get()
    programs=Programs.objects.all()
    
    course_det=course_details.objects.filter()[:1].get()
    context={'index':index,'programs':programs,'course_detail':course_det}
    
    return render(request, 'course.html', context)
    


def mail(request):

    return render(request, 'comingsoon_response.html')

def contact(request):
    index=Index.objects.filter()[:1].get()
    programs=Programs.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        response_email = render_to_string('response_email.html', {'name': name})
        mail = EmailMultiAlternatives('Thanks for response', response_email, settings.EMAIL_HOST_USER, [email,'shadmirza100@gmail.com'])
        mail.content_subtype = 'html'
        mail.send()

        send_mail('Message from CDOE Contact Form | Subject: '+subject, 'Name: '+name+'\n'+'Email: '+email+'\n'+'Subject: '+subject+'\n'+'Message: '+message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        return HttpResponseRedirect('contact')

    else:
        return render(request, 'contact.html', {'index': Index.objects.filter()[:1].get(), 'programs':programs})