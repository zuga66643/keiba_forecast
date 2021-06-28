from django import forms


class RaceForm(forms.Form):
    year = forms.CharField(label='year', max_length=4, initial='2021')
    place = forms.CharField(label='開催', max_length=4, initial='東京')
    num = forms.CharField(label='回', max_length=2, initial='1')
    day = forms.CharField(label='日目', max_length=2, initial='1')
    race = forms.CharField(label='R', max_length=2, initial='1')