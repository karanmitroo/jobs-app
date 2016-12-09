from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.

class Job(models.Model):
    id = models.AutoField(primary_key = True)
    title = models.CharField(max_length = 30)
    posted_on_date = models.DateTimeField(default=timezone.now)
    last_date = models.DateTimeField()
    annual_salary = models.IntegerField()
    description = models.TextField()
    location = models.TextField()
    url = models.URLField()
    experience = models.IntegerField()


    def __unicode__(self):
        return self.url
