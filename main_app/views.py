from django.shortcuts import render
from .models import News, Category
from django.utils import timezone
from datetime import timedelta


def index(request):
    categories = Category.objects.all()
    news_by_categories = {}

    filterargs = {}

    if 'today' in request.GET:
        if request.GET['today'] == '1':
            filterargs['created_at__range'] = [timezone.now().date(), timezone.now() + timedelta(days=1)]

    if 'cat' in request.GET:
        category = Category.objects.get(pk=request.GET['cat'])
        filterargs['category'] = request.GET['cat']
        news_by_categories = category.news.all()

    news = News.objects.filter(**filterargs)

    data = {
        'news': news,
        'categories': categories,
        'news_by_categories': news_by_categories
    }
    return render(request, 'index.html', context=data)


def edu(request):
    return render(request, 'edu/index.html')
