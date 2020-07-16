from django.shortcuts import render, redirect, HttpResponse
from .models import Dojo, Ninja

def index(request):
    # return render(request,'index.html')
    return HttpResponse('Hello Dojos & Ninjas')