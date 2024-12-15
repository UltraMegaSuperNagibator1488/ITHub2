from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from django.utils import timezone


def index(request):
    return render(request, 'index.html')


def tasks(request):
    tasks = Task.objects.all()

    data = {'tasks': tasks}
    return render(request, 'task/index.html', context=data)


def preparation_materials(request):
    return HttpResponse('<h1>Materials for preparation</h1>')
