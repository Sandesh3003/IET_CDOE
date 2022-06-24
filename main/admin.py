from django.contrib import admin

# Register your models here.
from .models import *


admin.site.site_header = "CDOE - DAVV Admin Panel"
admin.site.site_title = "CDOE - DAVV Admin Panel"

admin.site.register(Programs)
admin.site.register(course_details)
admin.site.register(course_categories)
admin.site.register(Review)
admin.site.register(course_type)
admin.site.register(course_head)
admin.site.register(Announcement)
admin.site.register(Notice)
admin.site.register(Faculty)
admin.site.register(Index)
admin.site.register(ComingSoonMailList)
admin.site.register(Slide)
admin.site.register(Student)
admin.site.register(useful_links)
admin.site.register(Team)

def send_newsletter(modeladmin, request, queryset):
    for newsletter in queryset:
        newsletter.send(request)

send_newsletter.short_description = "Send selected Mail to all subscribers"


class NewsletterAdmin(admin.ModelAdmin):
    actions = [send_newsletter]

admin.site.register(Newsletter, NewsletterAdmin)