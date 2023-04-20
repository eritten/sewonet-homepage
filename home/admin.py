from django.contrib import admin
from .models import Project

# Register your models here.


admin.site.register(Project)
admin.site.site_title = "Serwornet admin dashboard"
admin.site.site_header = "Serwornet admin dashboard"
