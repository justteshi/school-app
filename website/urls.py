from django.conf.urls import *
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('publications/', views.publications, name='publications'),
    path('teachers/', views.teachers, name='teachers'),
    path('history/', views.history, name='history'),
    path('documents/', views.documents, name='documents'),
    path('competitions/', views.competitions, name='competitions'),
    path('exams/', views.exams, name='exams'),
    path('admission/', views.admission, name='admission'),
    path('diary/', views.diary, name='school_diary'),
    path('contacts/', views.contacts, name='contacts'),
    path('more/', views.more, name='more'),
    path('budget/', views.budget, name='budget'),
    path('nastoiatelstvo/', views.nastoiatelstvo, name='nastoiatelstvo'),
    path('syllabus/', views.syllabus, name='syllabus'),
    path('login/', views.login, name='login'),
]