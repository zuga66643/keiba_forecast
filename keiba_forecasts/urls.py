from django.contrib import admin
from django.urls import path, include


from . import views


app_name = 'keiba_forecasts'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('blogs/', views.blogs, name='blogs'),
    path('blogs/<int:blog_id>', views.blog, name='blog'),
    path('blogs/<int:blog_id>/comments/', views.comments, name='comments'),
    path('dopester', views.dopester, name='dopester'),
]