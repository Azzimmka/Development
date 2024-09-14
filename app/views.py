from django.shortcuts import render, redirect, get_object_or_404
from .models import *
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




