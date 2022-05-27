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
    context={'announcements': announcement,'index':index,'programs':programs}
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
            'subhead_active': subhead_active,}
    if(len(courses)==0):
        return comingsoon(request) 
    else:
        return render(request, 'courses.html', context)
    
         


def notices(request):
    notice=Notice.objects.all()
    index=Index.objects.filter()[:1].get()
    return render(request, 'notices.html', {'notices': notice, 'index': index})

def course(request):
    index=Index.objects.filter()[:1].get()
    return render(request, 'course.html', {'index': index})

def courses(request,pk,ic):
    index=Index.objects.filter()[:1].get()
    return render(request, 'courses.html', {'index': index})

def mail(request):
    return render(request, 'comingsoon_response.html')

def contact(request):
    index=Index.objects.filter()[:1].get()

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
        return render(request, 'contact.html', {'index': Index.objects.filter()[:1].get()})