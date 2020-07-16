from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from django.contrib import messages

def index(request):
    return render (request, 'html.index')
