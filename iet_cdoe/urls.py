"""iet_cdoe URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views

from django.conf import settings
from django.conf.urls.static import static

from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from django.contrib import admin
from django_otp.admin import OTPAdminSite
  
admin.site.__class__ = OTPAdminSite

urlpatterns = [
    path('admin-webcd0e/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('contact', views.contact, name="contact"),
    path('faculty', views.faculty, name="faculty"),
    path('teams_s', views.team, name="team"),
    path('programs/<str:pk>', views.programs, name="programs"),
    path('programs/<str:pk>/<str:ic>', views.course, name="course"),
    path('notices', views.notices, name="notices"),
    path('course', views.course, name="course"),
    path('team', views.team, name="team"),
    path('compliance', views.compliance, name="compliance"),
    path('open_educational_resources', views.open_educational_resources, name="open_educational_resources"),
    path('sitemap.xml', views.sitemap, name="sitemap"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
