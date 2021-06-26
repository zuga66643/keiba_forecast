from django.contrib import admin
from django.urls import path, include


from . import views


app_name = 'keiba_forecasts'
urlpatterns = [
    path('', views.index, name='index'),
]