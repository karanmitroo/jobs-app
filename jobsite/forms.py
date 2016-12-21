from django import forms
from .models import Job, Country

class QueryForm(forms.Form):
    search = forms.CharField(required = True)
    location = forms.CharField(required = True)
    country = forms.ModelChoiceField(queryset = Country.objects.all())

class ContactForm(forms.Form):
	full_name = forms.CharField(required = False)
	email = forms.EmailField()
	subject = forms.CharField(required=False)
	message = forms.CharField()
