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
import json
import requests
from django.http import HttpResponse



# Create your views here.
# def prog(request,pk):
#     program=Program.objects.get(id=pk) 
#     context={'program':program}
#     return render(request,"main\course_page.html")


def index(request):
    
    index=Index.objects.filter()[:1].get()
    announcement=Announcement.objects.all()
    programs=Program.objects.all()
    context={'announcements': announcement,'index':index,'programs':programs}
    return render(request, 'index.html',context)

def comingsoon(request):
    index=Index.objects.filter()[:1].get()
    announcement=Announcement.objects.all()
    programs=Program.objects.all()
    context={'form': forms.ComingsoonForm(),'index':index,'programs':programs, 'announcements': announcement}
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
    programs=Program.objects.all()
    announcement=Announcement.objects.all()
    context={'faculty': Faculty.objects.all(),'index':index,'programs':programs, 'announcements': announcement}
    return render(request, 'faculty.html', context)

def team(request):
    index=Index.objects.filter()[:1].get()
    programs=Program.objects.all()
    announcement=Announcement.objects.all()
    context={'team': Team.objects.all(),'index':index,'programs':programs, 'announcements': announcement}
    return render(request, 'teams_s.html', context)

def programs(request,pk):
    index=Index.objects.filter()[:1].get()
    programs=Program.objects.all()
    announcement=Announcement.objects.all()
    context={'index':index,'programs':programs, 'announcements': announcement}
    subheads=CourseDetail.objects.filter(program_name=pk).values('course_type').distinct().all()
    su=list()
    for i in range(len(subheads)):
        x=subheads[i]['course_type']
        su.append(CourseType.objects.filter(course_type=x).get())
    courses=CourseDetail.objects.filter(program_name=pk).all()
    if(len(courses)==0):
        return comingsoon(request)
    subhead_active = su[0]
    subheads = su[1:]
    print(subheads)
    context={'index':index,'programs':programs,
            'courses':courses,'subheads':subheads, 
            'subhead_active': subhead_active,
            'program_name': pk}
    return render(request, 'courses.html', context)
    
def notices(request):
    notice=Notice.objects.all()
    index=Index.objects.filter()[:1].get()
    programs=Program.objects.all()
    announcement=Announcement.objects.all()
    return render(request, 'notices.html', {'notices': notice, 'index': index, 'programs':programs, 'announcements': announcement})

def course(request,pk,ic):
    index=Index.objects.filter()[:1].get()
    programs=Program.objects.all()
    announcement=Announcement.objects.all()
    # rating=Review.objects.filter(program_name__program_name=pk).filter(course_name=ic).values('rating').all()
    # reviews=Review.objects.filter(program_name__program_name=pk).filter(course_name=ic).all()
    
    # val=dict()
    # for rate in range(len(rating)):
    #     if rating[rate]['rating'] in val.keys():
    #         val[rating[rate]['rating']]=val[rating[rate]['rating']]+1
    #     else:
    #         val[rating[rate]['rating']]=1
    # maxi=0
    # if(len(rating)!=0):
    #     maxi=0
    #     fcount=0
    #     for x in val.keys():
    #          if(val[x]>fcount):
    #              fcount=val[x]
    #              maxi=x

    #     num_of_reviews=len(rating)
    # else:
    #     num_of_reviews="NO"
    # over_rate=range(maxi)
    # negative=range(5-maxi)
    course_det=CourseDetail.objects.filter(course_name=ic).filter(program_name__program_name=pk).get()
    context={'index':index,'programs':programs,'course_detail':course_det, 'announcements': announcement}
    return render(request, 'course.html', context)

def temp(request):
    index=Index.objects.filter()[:1].get()
    programs=Program.objects.all()
    announcement=Announcement.objects.all()
    
    course_det=CourseDetail.objects.filter()[:1].get()
    context={'index':index,'programs':programs,'course_detail':course_det, 'announcements': announcement}
    
    return render(request, 'course.html', context)
    


def mail(request):

    return render(request, 'comingsoon_response.html')

def contact(request):
    index=Index.objects.filter()[:1].get()
    programs=Program.objects.all()
    announcement=Announcement.objects.all()

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        #Recaptcha stuff
        
        clientKey = request.POST["g-recaptcha-response"]
        captchaSecretKey = '6Lf1xKIgAAAAABRbsHIBGCFGdO336r6YrUVDebxA'
        capthchaData = {
            'secret':captchaSecretKey,
            'response':clientKey
            }

        r = requests.post('https://www.google.com/recaptcha/api/siteverify',data=capthchaData)
        response = json.loads(r.text)
        verify = response['success']
        print('Captcha verification success :',verify)
        if verify:
            response_email = render_to_string('response_email.html', {'name': name})
            mail = EmailMultiAlternatives('Thanks for response', response_email, settings.EMAIL_HOST_USER, [email,'shadmirza100@gmail.com'])
            mail.content_subtype = 'html'
            mail.send()

            send_mail('Message from CDOE Contact Form | Subject: '+subject, 'Name: '+name+'\n'+'Email: '+email+'\n'+'Subject: '+subject+'\n'+'Message: '+message, settings.EMAIL_HOST_USER, [settings.EMAIL_HOST_USER])
            
            
            return HttpResponseRedirect('contact')
        else:
            return render(request, 'contact.html', {'index': Index.objects.filter()[:1].get(), 'programs':programs, 'announcements': announcement, 'verify':verify})
            # return HttpResponse('<script>alert("Captcha verification Failed");</script>')
        
    else:
        return render(request, 'contact.html', {'index': Index.objects.filter()[:1].get(), 'programs':programs, 'announcements': announcement})