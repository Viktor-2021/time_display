from django.http.request import HttpRequest
from django.shortcuts import redirect, render, HttpResponse 
from time import gmtime, strftime, localtime
import time

# Create your views here.

def root(request):
    return redirect('/style_display')

def index(request):
    context = {
        #"time":strftime("%Y-%m-%d %H:%M %p", gmtime())
        "timelocal":strftime("%d-%m-%Y %H:%M", localtime())
    }
    return render(request, 'index.html', context)