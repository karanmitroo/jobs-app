from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^search/(?P<search>[a-zA-z ]+)/(?P<location>[a-zA-z ]+)/(?P<country>[a-zA-z ]+)/page(?P<page>\d+)$', views.results, name = 'results'),
    url(r'^about$', views.about, name = 'about'),
	url(r'contact/$', views.contact, name = 'contact')
]
