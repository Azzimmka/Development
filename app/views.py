from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.http import Http404

# Create your views here.


def index(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'index.html', context)


def news(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'all_news.html', context)



def news_detail(request, news_slug):
    # Используем get_object_or_404 для обработки случаев, когда новость не найдена
    news = get_object_or_404(News, slug=news_slug)
    
    context = {
        'news': news
    }
    return render(request, 'news_detail.html', context)



def license_view(request):
    licenses = License.objects.all()  # Получаем все объекты
    return render(request, 'license.html', {'licenses': licenses})

