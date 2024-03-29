from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from geopy.geocoders import Nominatim
from mapper.models import Location


__author__ = 'j3dev'


class EmailUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def clean_username(self):
        # Since User.username is unique, this check is redundant,
        # but it sets a nicer error message than the ORM. See #13147.
        username = self.cleaned_data["username"]
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username'],
            code='duplicate_username',
        )


class LocationForm(forms.Form):
    name = forms.CharField()#label='Here\'s lookin\' at you, kid.', max_length=100)

    gelocator = Nominatim()
    mappy = Location.objects.get()
    location = gelocator.geocode(mappy)