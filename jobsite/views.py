from django.shortcuts import render, redirect
from .models import Job
from .forms import QueryForm
import requests, json
import os
# Create your views here.

def home(request):
    form = QueryForm(request.POST or None)

    if form.is_valid():
        search = form.cleaned_data.get('search')
        location = form.cleaned_data.get('location')

        return redirect(results, search = search, location = location, page = 0)

        # response = requests.get("http://api.indeed.com/ads/apisearch?publisher=7730342108690608" + "&q="+search + "&l="+location + "&sort=&radius=40&st=&jt=&start=&end=&limit=100&format=json&fromage=&filter=&latlong=1" + "&co=in" + "&chnl=&userip=122.162.34.161&useragent=Mozilla/%2F4.0%28Firefox%29&v=2")
        # total_results = json.loads(response.text)["totalResults"]
        # for i in range(0, total_results, 25):
        #     response = requests.get("http://api.indeed.com/ads/apisearch?publisher=7730342108690608" + "&q="+search + "&l="+location + "&sort=&radius=40&st=&jt=" + "&start="+str(i+1) + "&end="+str(i+25) + "&limit=100&format=json&fromage=&filter=&latlong=1" + "&co=in" + "&chnl=&userip=122.162.34.161&useragent=Mozilla/%2F4.0%28Firefox%29&v=2")
        #     data = json.loads(response.text)



    return render(request, 'jobsite/home.html', {'form' : form})

def results(request, search, location, page):

    start = 25 * (int(page) - 1)
    response_indeed = requests.get("http://api.indeed.com/ads/apisearch?publisher=7730342108690608" + "&q="+search + "&l="+location + "&sort=&radius=40&st=&jt=" + "&start="+str(start+1) + "&end="+str(start+25) + "&limit=100&format=json&fromage=&filter=&latlong=1" + "&co=in" + "&chnl=&userip=122.162.34.161&useragent=Mozilla/%2F4.0%28Firefox%29&v=2")
    data_indeed = json.loads(response_indeed.text)["results"]

    with open('/home/karan/Desktop/jobs/jobsite/data/countrycodes.json') as countrycodes:
        countrycodesjson = json.loads(countrycodes.read())

    for i in range(0, len(countrycodesjson)):
        if countrycodesjson[i]["country"].upper() == location.upper():
            country = countrycodesjson[i]["code"]
            print country

    link = "http://service.dice.com/api/rest/jobsearch/v1/simple.json?" + "text=" +search+ "&state=location"

    if 'country' in locals():
         link += "&country="+country

    response_dice = requests.get(link)
    data_dice = json.loads(response_dice.text)["resultItemList"]
    return render(request, 'jobsite/joblist.html', {'data' : data_indeed})
