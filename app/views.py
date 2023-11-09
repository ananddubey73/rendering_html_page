from django.shortcuts import render
from app.views import *

# Create your views here.

def macha(request):
    return render(request,'Tamplate.html')