from django import forms


class RaceForm(forms.Form):
    year = forms.CharField(label='year', max_length=4, initial='2021')
    c_place = []
    p_name = ['札幌','函館','福島','新潟','東京','中山','中京','京都','阪神','小倉']
    for p in p_name:
        c_place.append((p,p))
    place = forms.ChoiceField(label='開催', initial='東京', choices=c_place)
    c_num = []
    for i in range(1,7):
        c_num.append((str(i),str(i)))
    num = forms.ChoiceField(label='回', initial='1', choices=c_num)
    c_day = []
    for i in range(1,13):
        c_day.append((str(i),str(i)))
    day = forms.ChoiceField(label='日目', initial='1', choices=c_day)
    c_race = []
    for i in range(1,13):
        c_race.append((str(i),str(i)))
    race = forms.ChoiceField(label='R', initial='1', choices=c_race)

