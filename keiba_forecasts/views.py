from django.shortcuts import render

from .forms import RaceForm

from .models import Blog

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = RaceForm(request.POST)
        content_dict = {'form':form}
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
        
        year = str(content_dict['year'])
        race_id = year + place_num + num + day + race
        

        src = f'/static/{race_id}deployment.png'

        place = content_dict['place']
        content_dict['info'] = f'{year}年 {place} {num}回 {day}日目 {race}R'
        content_dict['src'] = src
        content_dict['id'] = race_id
    else:
        form = RaceForm()
        content_dict = {'form':form}


    return render(request, 'keiba_forecasts/index.html', content_dict)


def about(request):
    return render(request, 'keiba_forecasts/about.html')


def blogs(request):
    blogs = Blog.objects.order_by('date')
    context = {'blogs':blogs}
    return render(request, 'keiba_forecasts/blogs.html', context)


def blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {
        'blog':blog,
        'text':blog.text,
        'date':blog.date,
    }
    return render(request, 'keiba_forecasts/blog.html', context)
