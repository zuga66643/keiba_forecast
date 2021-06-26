from django.shortcuts import render

from .forms import RaceForm

# Create your views here.
def index(request):
    form = RaceForm()
    content_dict = {'form':form}
    if request.method == 'POST':
        content_dict['year'] = request.POST.get('year', None)
        content_dict['place'] = request.POST.get('place', None)
        content_dict['num'] = request.POST.get('num', None)
        content_dict['day'] = request.POST.get('day', None)
        content_dict['race'] = request.POST.get('race', None)


        place_list = ['札幌','函館','福島','新潟','東京','中山','中京','京都','阪神','小倉']
        i = 1
        for p in place_list:
            if content_dict['place'] == p:
                place_num = i
            i += 1
        
        if place_num < 10:
            place_num = '0' + str(place_num)

        if int(content_dict['num']) < 10:
            num = '0' + content_dict['num']
        else:
            num = content_dict['num']

        if int(content_dict['day']) < 10:
            day = '0' + content_dict['day']
        else:
            day = content_dict['day']

        if int(content_dict['race']) < 10:
            race = '0' + content_dict['race']  
        else:
            race =  content_dict['race']  
        
        race_id = str(content_dict['year']) + place_num + num + day + race
        

        src = f'/static/{race_id}deployment.png'

        content_dict['src'] = src
        content_dict['id'] = race_id
    else:
        pass


    return render(request, 'keiba_forecasts/index.html', content_dict)



