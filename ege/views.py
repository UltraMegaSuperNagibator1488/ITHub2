from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse('<h1>Ege main page</h1><a href="tasks/">Tasks list</a><br><a href="preparation/">Preparation materials</a>')


def tasks_main_page(request):
    return HttpResponse('<h1>List of tasks</h1>')


def tasks(request, task_id):
    return HttpResponse(f'<h1>Task №{task_id}</h1>')


def preparation_materials(request):
    return HttpResponse('<h1>Materials for preparation</h1>')
