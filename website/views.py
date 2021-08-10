from django.shortcuts import render
from django.http import Http404
from .models import Budget, HomePageMessages, Teacher, Publication, Budget

# Create your views here.

def home(request):
    template = 'home.html'
    articles = HomePageMessages.objects.all()

    context = {
        'articles': articles.order_by('-created_at')
    }

    return render(request, template, context)

def messages_detail_view(request, id):
    try:
        message = HomePageMessages.objects.filter(id=id)
    except HomePageMessages.DoesNotExist:
        return Http404()
    
    template = 'message_page.html'
    context = {
        'message': message
    }
    
    return render(request, template, context)

def publications(request):
    template = 'publications.html'
    publications = Publication.objects.all()
    context = {
        'publications' : publications
    }
    return render(request, template, context)
    
def teachers(request):
    template = 'teachers.html'
    teachers = Teacher.objects.all()
    context = {
        'teachers': teachers
    }
    return render(request, template, context)

def history(request):
    template = 'history.html'
    context = {}

    return render(request, template, context)

def budget(request):
    template = 'budget.html'

    budgets = Budget.objects.all()
    years = Budget.objects.values_list('year', flat=True)
    years_list = []
    for year in years:
        if year in years_list:
            continue
        else:
            years_list.append(year)

    context = {
        'budgets': budgets,
        'years_list': years_list[::-1],
    }

    return render(request, template, context)

def nastoiatelstvo(request):
    template = 'nastoiatelstvo.html'
    context = {}

    return render(request, template, context)

def schedule(request):
    template = 'schedules.html'
    context = {}

    return render(request, template, context)

def syllabus(request):
    template = 'syllabus.html'
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
