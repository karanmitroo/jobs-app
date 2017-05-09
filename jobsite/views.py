from django.shortcuts import render, redirect
from .models import Job
from .forms import QueryForm, ContactForm
import requests, json
# import os
# Create your views here.

def home(request):
    form = QueryForm(request.POST or None)

    if form.is_valid():
        search = form.cleaned_data.get('search')
        location = form.cleaned_data.get('location')
        country = str(form.cleaned_data.get('country'))

        return redirect("/search/" + search + "/" + location + "/" + country + "/" "page0")

    return render(request, 'jobsite/home.html', {'form' : form})

def results(request, search, location, country, page):


    # for i in range(0, len(countrycodesjson)):
    #     if countrycodesjson[i]["country"].upper() == country.upper():
    #         country = countrycodesjson[i]["code"].lower()
    #         print country


    start = 25 * (int(page) - 1)

    link_indeed = "http://api.indeed.com/ads/apisearch?publisher=7730342108690608" + "&q="+search + "&l="+location + "&sort=date&radius=40&st=&jt=" + "&start="+str(start+1) + "&end="+str(start+25) + "&limit=100&format=json&fromage=&filter=&latlong=1" + "&co=US" + "&chnl=&userip=122.162.34.161&useragent=Mozilla/%2F4.0%28Firefox%29&v=2"
    response_indeed = requests.get(link_indeed)
    data_indeed = json.loads(response_indeed.text)["results"]

    # with open('/home/karan/Desktop/jobs/jobsite/data/countrycodes.json') as countrycodes:
    #     countrycodesjson = json.loads(countrycodes.read())
    #
    # for i in range(0, len(countrycodesjson)):
    #     if countrycodesjson[i]["country"].upper() == location.upper():
    #         country = countrycodesjson[i]["code"]
    #         print country


    link_dice = "http://service.dice.com/api/rest/jobsearch/v1/simple.json?" + "text=" +search + "&state="+location + "&country=US"

    # if 'country' in locals():
    #      link_dice += "&country="+country

    response_dice = requests.get(link_dice)
    data_dice = json.loads(response_dice.text)["resultItemList"]


    form = QueryForm(request.POST or None)

    if form.is_valid():
        search = form.cleaned_data.get('search')
        location = form.cleaned_data.get('location')
        country = str(form.cleaned_data.get('country'))

        return redirect("/search/" + search + "/" + location + "/" + country + "/" "page0")

    data = {
    'data_indeed' : data_indeed,
    'data_dice' : data_dice,
    'form' : form
    }
    return render(request, 'jobsite/joblist.html', data)


def about(request):
    data = {'about_us' : "This is the about us page. This is the about us page. This is the about us page. This is the about us page. This is the about us page. This is the about us page. This is the about us page. This is the about us page. This is the about us page."}

    return render(request, 'about.html', data)

def contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		form.save()
		return render(request, 'home.html')

	return render(request, 'contact.html', {'form': form})
