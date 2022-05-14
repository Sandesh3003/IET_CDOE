import email
import imp
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import *
# Create your views here.
def prog(request,pk):
    program=Program.objects.get(id=pk) 
    context={'program':program}
    return render(request,"main\course_page.html")


def index(request):
    program=Program.objects.all()
    announcement=Announcement.objects.all()
    context={'programs':program, 'announcements': announcement}
    return render(request, 'index.html',context)

def comingsoon(request):
    return render(request, 'coming_soon.html')

def faculty(request):
    return render(request, 'faculty.html', {'faculty': Faculty.objects.all()})

def online_programs(request):
    return render(request, 'coming_soon.html')

def distance_learning_programs(request):
    return render(request, 'coming_soon.html')

def notices(request):
    notice=Notice.objects.all()
    return render(request, 'notices.html', {'notices': notice})

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
        return render(request, 'contact.html')