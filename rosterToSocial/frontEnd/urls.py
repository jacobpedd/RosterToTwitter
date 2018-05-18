from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^findTwitter/(?P<pk>\d+)$', views.find_twitter, name='find_twitter'),
    url(r'^roster/(?P<pk>\d+)$', views.roster_details, name='roster'),
    url(r'^selectTwitterResult/(?P<pk>\d+)$', views.select_twitter_result, name='select_twitter_result'),
    url(r'^noTwitter/(?P<pk>\d+)$', views.no_twitter, name='no_twitter'),
    url(r'^removeTwitter/(?P<pk>\d+)$', views.remove_twitter, name='remove_twitter'),
    url(r'^removeRoster/(?P<pk>\d+)$', views.remove_roster, name='remove_roster'),
    url(r'^downloadRoster/(?P<pk>\d+)$', views.download_roster, name='download_roster'),
    url(r'^rosterFromUrl$', views.roster_from_url, name='roster_from_url'),
]