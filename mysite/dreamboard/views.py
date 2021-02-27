from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import dream
from .forms import DreamForm

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
        return render(request, 'dreamboard/addDream.html', {'form':form, 'dreamboard_dream': dream.objects.all()})
        #return redirect('index')
