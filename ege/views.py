from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from django.utils import timezone


def index(request):
    return HttpResponse('<h1>Ege main page</h1><a href="tasks/">Tasks list</a><br><a href="preparation/">Preparation materials</a>')


def tasks(request):
    tasks = Task.objects.all()

    data = {'tasks': tasks}
    return render(request, 'task/index.html', context=data)


def preparation_materials(request):
    return HttpResponse('<h1>Materials for preparation</h1>')
