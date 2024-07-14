from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1>Get ready for Oge</h1>')


def tasks(requests):
    return HttpResponse('<h1>Best tasks for prepearing to Oge</h1>')


def theory(requests):
    return HttpResponse('<h1>Base theory for prepearing to Oge</h1>')


def tasks_number(requests, slug_id):
    return HttpResponse(f'<h2>Your number is {slug_id}</h2>')
