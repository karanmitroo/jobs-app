from django.contrib import admin
from .models import *

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ['title', '__unicode__']

    class Meta:
        model = Job


class CountryAdmin(admin.ModelAdmin):
    list_display = ['country', 'code']
    class Meta:
        model = Country

admin.site.register(Job, JobAdmin)
admin.site.register(Country, CountryAdmin)
