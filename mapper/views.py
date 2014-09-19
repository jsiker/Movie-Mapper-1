from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, render_to_response
import urllib2
from BeautifulSoup import BeautifulSoup
from .forms import EmailUserCreationForm, LocationForm
from mapper import forms
from mapper.models import Location
from movie_mapper import settings
from django import forms
from django.shortcuts import render_to_response
from gmapi import maps
from gmapi.forms.widgets import GoogleMap

@login_required()
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = EmailUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # user.email_user("Welcome, {}!, Thank you for signing up for our website.".format(user.username))
            text_content = "Thank you for signing up on {} for our website, {} {}".format(user.date_joined, user.first_name, user.last_name)
            html_content = "<h2>Thanks {} {} for signing up on {}!</h2> <div>I hope you enjoy using my site</div>".format(user.first_name, user.last_name, user.date_joined)
            msg = EmailMultiAlternatives("Welcome!", text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
            return redirect("home")
    else:
        form = EmailUserCreationForm()

    return render(request, "registration/register.html", {
        'form': form,
    })

@login_required
def profile(request):
    data = {"location_form": LocationForm()}
    if request.method == 'POST':
        data = {"location_form": LocationForm()}
        form = LocationForm(request.POST)
        if form.is_valid():
            Location.objects.create(name=form.cleaned_data['name'])
            return HttpResponseRedirect('profile')
    else:
        data = {"location_form": LocationForm()}
    return render(request, 'profile.html', data)


class MapForm(forms.Form):
    map = forms.Field(widget=GoogleMap(attrs={'width':510, 'height':510}))


def index(request):
    gmap = maps.Map(opts = {
        'center': maps.LatLng(38, -97),
        'mapTypeId': maps.MapTypeId.ROADMAP,
        'zoom': 3,
        'mapTypeControlOptions': {
             'style': maps.MapTypeControlStyle.DROPDOWN_MENU
        },
    })
    context = {'form': MapForm(initial={'map': gmap})}
    return render_to_response('index.html', context)
# gmap = maps.Map
#     marker = maps.Marker(opts = {
#         'map': gmap,
#         'position': maps.LatLng(38, -97),
#     })
#     maps.event.addListener(marker, 'mouseover', 'myobj.markerOver')
#     maps.event.addListener(marker, 'mouseout', 'myobj.markerOut')
#     info = maps.InfoWindow({
#         'content': 'Hello!',
#         'disableAutoPan': True
#     })
#     info.open(gmap, marker)
