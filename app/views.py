from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.


def index(request):
    news = News.objects.all()
    context = {
        'news': news
    }
    return render(request, 'index.html', context)


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

def person(request):
    context = {
        'persons': Person.objects.all()
    }
    return render(request, 'persons.html', context)


def structure(request):
    return render(request, 'structure.html')

def tenders(request):
    context = {
        'tenders': Tenders.objects.all()
    }
    return render(request, 'tenders.html', context)



def financе(request):
    years = Year.objects.all().order_by('year')  
    financial_data = FinancialData.objects.all() 
    context = {
        'years': years,
        'financial_data': financial_data,
    }
    return render(request, 'finance.html', context)


def boshqaruv(request):
    management = Management.objects.all()
    context = {
        'management': management,
    }
    return render(request, 'boshqaruv.html', context)

def more_info(request):
    info = MoreInfo.objects.all()
    context = {
        'info': info,
    }
    return render(request, 'more_info.html', context)

def department(request):
    return render(request, 'department.html')