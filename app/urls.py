from django.urls import path
from .views import *

urlpatterns = [ 
    path('', index, name='index'),
    path('person/', person, name='person'),
    path('tenders/', tenders, name='tenders'),
    path('finance/', financе, name='finance'),
    path('license/', license_view, name='license'),
    path('boshqaruv/', boshqaruv, name='boshqaruv'),
    path('structure/', structure, name='structure'),
    path('more_info/', more_info, name='more_info'),
    path('department/', department, name='department'),
    path('news/<slug:news_slug>/', news_detail, name='news_detail'),

]
