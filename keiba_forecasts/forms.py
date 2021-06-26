from django import forms


class RaceForm(forms.Form):
    year = forms.CharField(label='year', max_length=4)
    place = forms.CharField(label='開催', max_length=4)
    num = forms.CharField(label='回', max_length=2)
    day = forms.CharField(label='日目', max_length=2)
    race = forms.CharField(label='R', max_length=2)