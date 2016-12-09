from django import forms
from .models import Job

class QueryForm(forms.Form):
    search = forms.CharField(required = True)
    location = forms.CharField(required = False)
