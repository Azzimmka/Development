from django.urls import path
from .views import *

urlpatterns = [ 
    path('', index, name='index'),
    path('news/', news, name='news'),
    path('license/', license_view, name='license'),
    path('news/<slug:news_slug>/', news_detail, name='news_detail'),
]
