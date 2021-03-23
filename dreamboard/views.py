from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import dream
from .forms import DreamForm, CreateUserForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm

from django.views.generic.base import TemplateView

from . import urls

# Create your views here.


def index(request):
    return render(request, 'dreamboard/index.html', {'dreamboard_dream': dream.objects.all()})


def home(request):
    return render(request, 'dreamboard/home.html')


def addDream(request):



    if request.method == "GET":
        form = DreamForm()
        return render(request, 'dreamboard/addDream.html', {'form':form, 'dreamboard_dream': dream.objects.all()})
    else:
        form = DreamForm(request.POST)
        if form.is_valid():
            form.save()
        # return render(request, 'dreamboard/addDream.html', {'form':form, 'dreamboard_dream': dream.objects.all()})
        return redirect('index')

def displayDream(request, pk):
    dreamObject = dream.objects.get(id=pk)

    context = {'dreamObject' : dreamObject}

    return render(request, 'dreamboard/displayDream.html', context)


def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)

            return redirect('login')


    context = {'form':form}
    return render(request, 'dreamboard/register.html', context)

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Username OR password is incorrect')
            return render(request, 'dreamboard/login.html', context)

    context = {}

    return render(request, 'dreamboard/login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')







    return render(request, 'dreamboard/logout.html')
