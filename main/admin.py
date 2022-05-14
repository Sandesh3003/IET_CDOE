from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Program)
admin.site.register(Announcement)
admin.site.register(Notice)
admin.site.register(Faculty)