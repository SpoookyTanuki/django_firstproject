from django.shortcuts import render, reverse
from django.http import HttpResponse
from datetime import datetime
import os

def home_view(request):
    return HttpResponse(f'Hello Django')

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    current_time = datetime.now()
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    workdir = "/Users/elenapalenova/Desktop/パイソン paison/homeworks/block_4_django/dj-homeworks/first-project"
    dirs = os.listdir(workdir)
    file_list = []
    for file in dirs:
        file_list.append(file)
        file_list.append('</br>')
    return HttpResponse(file_list)

    # raise NotImplemented
