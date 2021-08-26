from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, RegisterForm
from .models import Budget, HomePageMessages, Teacher, Publication, Budget
from .filters import TeacherFilter
from django.contrib.auth.models import User

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
    teachers_filter = TeacherFilter(request.GET, queryset=teachers)
    teachers = teachers_filter.qs
    context = {
        'teachers_filter': teachers_filter,
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

def class_tests(request):
    template = 'class_tests.html'
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

def register_view(request):
    if request.method == "GET":
        form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            password2 = form.cleaned_data.get('password2')
            try:
                user = User.objects.create_user(username, email, password1)
            except:
                user = None

            if user != None:
                login(request, user)
                return redirect('/')
            else:
                request.session['register_error'] = 1

    return render(request, 'register.html', {
                'form': form
            })

def login_view(request):
    if request.method == 'GET':
        form = LoginForm()

    if request.method == 'POST':
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user != None:
                login(request, user)
                return redirect('/')
            else:
                # attempt = request.session.get('attempt') or 0
                # request.session['attempt'] = attempt + 1
                request.session['invalid_user'] = 1
    

    return render(request, 'login.html', {
                'form': form,
            })


def logout_view(request):
    logout(request)
    return redirect('/login')