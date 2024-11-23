from django.urls import path

from . import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('about', views.about , name = 'about'),
    path('m1', views.m1 , name = 'm1'),
    path('m2', views.m2 , name = 'm2'),
    path('m3', views.m3 , name = 'm3'),
    path('m4', views.m4 , name = 'm4'),
    path('m5', views.m5 , name = 'm5'),
    path('m6', views.m6 , name = 'm6')
]


