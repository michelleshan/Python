from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse('Hello!!!')

def cats(request, cat_name):
    chese = 5 * cat_name
    return HttpResponse(f"{chese}")
