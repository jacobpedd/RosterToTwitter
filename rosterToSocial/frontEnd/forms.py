from django import forms
from django.core.exceptions import ValidationError

from .models import Roster, Player


# Form on the landing page that takes a column and a file
class RosterForm(forms.ModelForm):
    name_col = forms.CharField(label='Name Column (A-Z)')
    twitter_col = forms.CharField(label='Twitter Column (A-Z)')
    document = forms.FileField(label='')

    class Meta:
        model = Roster
        fields = ('name_col', 'twitter_col', 'document')


# Validates that the ESPN url is proper
def validate_url(url):
    if not str(url).__contains__('espn.com') or not str(url).__contains__('/roster/'):
        raise ValidationError('Not a valid ESPN roster URL')


# Takes an ESPN url for scraping
class RosterFromUrl(forms.Form):
    url = forms.URLField(label='URL', validators=[validate_url])

    class Meta:
        fields = ('url',)


# Changes the search term on the add twitter
class TwitterSeachTermForm(forms.ModelForm):
    name = forms.CharField(required=False, label='Term')

    class Meta:
        model = Player
        fields = ('name',)


# Form for changing a rosters name
class RosterNameForm(forms.ModelForm):
    name = forms.CharField(required=False)

    class Meta:
        model = Roster
        fields = ('name',)


# Form for changin a rosters minimum followers
class RosterMinForm(forms.ModelForm):
    min_followers = forms.CharField(required=False, label='Minimum followers')

    class Meta:
        model = Roster
        fields = ('min_followers',)
