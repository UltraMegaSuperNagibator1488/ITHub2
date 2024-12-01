from django.shortcuts import render
from .models import News
from django.utils import timezone
from datetime import timedelta


def index(request):
    filterargs = {}

    if 'today' in request.GET:
        if request.GET['today'] != '0':
            filterargs['created_at__range'] = [timezone.now().date(), timezone.now() + timedelta(days=1)]

    if 'cat' in request.GET:
        filterargs['category'] = request.GET['cat']

    news = News.objects.filter(**filterargs)

    data = {'news': news}
    return render(request, 'index.html', context=data)


def edu(request):
    return render(request, 'edu/index.html')
