from django.shortcuts import render
from .models import News


def index(request):
    news = News(title='news 1', desc='description of first news')
    print(news)
    return render(request, 'index.html')


def edu(request):
    return render(request, 'edu/index.html')
