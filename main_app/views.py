from django.shortcuts import render
from .models import News
from datetime import timezone, timedelta


def index(request):
    if 'today' in request.GET:
        if request.GET['today'] != '0':
            news = News.objects.filter(created_at__range=[timezone.now().date(), timezone.now() + timedelta(days=1)])
            data = {'news': news}
            return render(request, 'index.html', context=data)

    news = News.objects.all()
    data = {'news': news}
    return render(request, 'index.html', context=data)

def edu(request):
    return render(request, 'edu/index.html')
