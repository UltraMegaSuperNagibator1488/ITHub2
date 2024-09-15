from django.http import HttpResponse
from django.shortcuts import render


class Task:

    def __init__(self, id: int, ege_num: int, desc: str, ege_data: int | None):
        self.id = id
        self.ege_num = ege_num
        self.desc = desc
        self.ege_data = ege_data

task1 = Task(1, 27, 'aaaa', 2020)
task2 = Task(2, 25, 'bbbb', None)


def index(request):
    return HttpResponse('<h1>Ege main page</h1><a href="tasks/">Tasks list</a><br><a href="preparation/">Preparation materials</a>')


def tasks(request):
    return render(request, 'task/index.html', context={'tasks': [task1, task2]})


def preparation_materials(request):
    return HttpResponse('<h1>Materials for preparation</h1>')
