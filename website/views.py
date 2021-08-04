from django.shortcuts import render
from django.http import Http404
from .models import HomePageArticle, Teacher, Publication

# Create your views here.

def home(request):
    template = 'home.html'
    articles = HomePageArticle.objects.all()
    context = {
        'articles': articles
    }

    return render(request, template, context)

def publications(request):
    template = 'publications.html'
    publications = Publication.objects.all()
    context = {
        'publications' : publications
    }
    return render(request, template, context)

def about(request):
    template = 'about.html'
    employees = Teacher.objects.all()
    context = {
        'employees': employees
    }

    return render(request, template, context)

def schedules(request):
    template = 'schedules.html'
    context = {}

    return render(request, template, context)

def documents(request):
    template = 'documents.html'
    context = {}

    return render(request, template, context)

def competitions(request):
    template = 'competitions.html'
    context = {}

    return render(request, template, context)

def exams(request):
    template = 'exams.html'
    context = {}

    return render(request, template, context)

def admission(request):
    template = 'admission.html'
    context = {}

    return render(request, template, context)

def diary(request):
    template = 'school_diary.html'
    context = {}

    return render(request, template, context)

def contacts(request):
    template = 'contacts.html'
    context = {}

    return render(request, template, context)

def more(request):
    template = 'more.html'
    context = {}

    return render(request, template, context)

def login(request):
    template = 'login.html'
    context = {}

    return render(request, template, context)
