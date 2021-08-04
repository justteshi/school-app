from django.conf.urls import *
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('schedules/', views.schedules, name='schedules'),
    path('documents/', views.documents, name='documents'),
    path('competitions/', views.competitions, name='competitions'),
    path('exams/', views.exams, name='exams'),
    path('admission/', views.admission, name='admission'),
    path('diary/', views.diary, name='school_diary'),
    path('contacts/', views.contacts, name='contacts'),
    path('more/', views.more, name='more'),
    path('login/', views.login, name='login'),
]