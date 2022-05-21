import email
import imp
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import *

# Create your views here.
# def prog(request,pk):
#     program=Program.objects.get(id=pk) 
#     context={'program':program}
#     return render(request,"main\course_page.html")


def index(request):
    program=Program.objects.all()
    Content=index_content.objects.filter()[:1].get()
    announcement=Announcement.objects.all()
    Footer=footer.objects.filter()[:1].get()
    context={'programs':program, 'announcements': announcement,'Content':Content,'Footer':Footer}
    return render(request, 'index.html',context)

def comingsoon(request):
    if request.method == 'POST':
        email = request.POST['email']
        x = EmailComingSoon(email=email)
        x.save()
    return render(request, 'coming_soon.html', {'Footer': footer.objects.filter()[:1].get()})

def faculty(request):
    return render(request, 'faculty.html', {'faculty': Faculty.objects.all(), 'Footer': footer.objects.filter()[:1].get()})

def online_programs(request):
    return render(request, 'coming_soon.html', {'Footer': footer.objects.filter()[:1].get()})

def distance_learning_programs(request):
    return render(request, 'coming_soon.html', {'Footer': footer.objects.filter()[:1].get()})

def notices(request):
    notice=Notice.objects.all()
    return render(request, 'notices.html', {'notices': notice, 'Footer': footer.objects.filter()[:1].get()})

def course(request):
    return render(request, 'course.html', {'Footer': footer.objects.filter()[:1].get()})

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        response_email = render_to_string('response_email.html', {'name': name})
        mail = EmailMultiAlternatives('Thanks for response', response_email, settings.EMAIL_HOST_USER, [email])
        mail.content_subtype = 'html'
        mail.send()

        send_mail('Message from CDOE Contact Form | Subject: '+subject, 'Name: '+name+'\n'+'Email: '+email+'\n'+'Subject: '+subject+'\n'+'Message: '+message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
        return HttpResponseRedirect('contact')

    else:
        return render(request, 'contact.html', {'Footer': footer.objects.filter()[:1].get()})