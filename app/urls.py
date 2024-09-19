from django.urls import path
from .views import *

urlpatterns = [ 
    path('', index, name='index'),
    path('person/', person, name='person'),
    path('tenders/', tenders, name='tenders'),
    path('finance/', financе, name='finance'),
    path('license/', license_view, name='license'),
    path('structure/', structure, name='structure'),
    path('news/<slug:news_slug>/', news_detail, name='news_detail'),

]
