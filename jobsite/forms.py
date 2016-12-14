from django import forms
from .models import Job, Country

class QueryForm(forms.Form):
    search = forms.CharField(required = True)
    location = forms.CharField(required = True)
    country = forms.ModelChoiceField(queryset = Country.objects.all())
