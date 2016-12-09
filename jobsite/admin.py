from django.contrib import admin
from .models import *

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', '__unicode__']

    class Meta:
        model = Job

admin.site.register(Job, JobAdmin)
