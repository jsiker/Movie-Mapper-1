import re
from django.contrib.sessions import serializers
from django.core.serializers import json
import urllib2
# from movie_mapper.mapper.models import Movie
from bs4 import BeautifulSoup

# The actual query
# def getid():
#     searchstring = Movie.name.objects.all()
#     year = Movie.year.objects.all()
#     url = "http://www.imdbapi.com/?t=" + searchstring + "&y="+year
#     request = urllib2.Request(url)
#     response = json.load(urllib2.urlopen(request))
#     print json.dumps(response, indent=2)
#     data = serializers.serialize('json', ['imdbID'])
#     return data
#
# def scrape_id(data):
#     page = urllib2.urlopen("http://www.imdb.com/title/" + data + "/locations?ref_=tt_dt_dt")
#     soup = BeautifulSoup(page)
#     for incident in soup(text=re.compile(r'itemprop="url">')):
#         # where = incident.contents[0:]
#         print incident
#
# # getid()
# scrape_id('tt0066999')

# BASE_URL = "http://www.imdb.com"
#
# def get_category_links(section_url):
#     html = urllib2.urlopen(section_url).read()
#     soup = BeautifulSoup(html, "lxml")
#     boccat = soup.find("dl", "boccat")
#     category_links = [BASE_URL + dd.a["href"] for dd in boccat.findAll("dd")]
#     return category_links




def search_locs():
    html = urllib2.urlopen('http://www.imdb.com/title/tt2872732/locations?ref_=tt_dt_dt')
    soup = BeautifulSoup(html)
    dt = soup.find_all('dt')
    #dt = dt.encode('ascii', 'ignore')
    # place = str(dt[2].get_text())
    # print place
    for d in dt:
        place = d.get_text()
        print place



search_locs()