from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Program)
admin.site.register(Announcement)
admin.site.register(Notice)
admin.site.register(Faculty)
admin.site.register(index_content)
admin.site.register(EmailComingSoon)
admin.site.register(footer)