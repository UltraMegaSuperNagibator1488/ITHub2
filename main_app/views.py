from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def edu(request):
    return render(request, 'edu/index.html')
