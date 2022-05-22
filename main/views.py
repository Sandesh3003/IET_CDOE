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
    program=Program.objects.all()
    index=Index.objects.filter()[:1].get()
    announcement=Announcement.objects.all()
    context={'programs':program, 'announcements': announcement,'index':index}
    return render(request, 'index.html',context)

def comingsoon(request):
    index=Index.objects.filter()[:1].get()
    if request.method == 'POST':
        emailid = request.POST['email']
        sub = ComingSoonMailList(email=emailid)
        sub.save()
        return render(request, 'coming_soon.html', {'form': forms.ComingsoonForm(), 'index': index})
    else:
        return render(request, 'coming_soon.html', {'form': forms.ComingsoonForm(), 'index': index}) 

def faculty(request):
    index=Index.objects.filter()[:1].get()
    return render(request, 'faculty.html', {'faculty': Faculty.objects.all(), 'index': index})

def online_programs(request):
    index=Index.objects.filter()[:1].get()
    return render(request, 'coming_soon.html', {'index': index})

def distance_learning_programs(request):
    index=Index.objects.filter()[:1].get()
    return render(request, 'coming_soon.html', {'index': index})

def notices(request):
    notice=Notice.objects.all()
    index=Index.objects.filter()[:1].get()
    return render(request, 'notices.html', {'notices': notice, 'index': index})

def course(request):
    index=Index.objects.filter()[:1].get()
    return render(request, 'course.html', {'index': index})
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
        return render(request, 'contact.html', {'index': index})