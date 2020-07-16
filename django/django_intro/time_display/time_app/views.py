from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

def index(request):
    context = {
        'date': strftime('%B %d, %Y'),
        'time': strftime('%H:%M %p',gmtime())
    }
    return render(request,'index.html',context)

