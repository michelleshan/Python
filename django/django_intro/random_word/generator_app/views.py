from django.shortcuts import render, redirect, HttpResponse
from django.utils.crypto import get_random_string

def index(request):
    if 'attempt' not in request.session:
        request.session['attempt'] = 0
        print('not in session')
    return render(request,'index.html')

def random_word(request):
    request.session['attempt'] += 1
    request.session['random'] = get_random_string(length=14)
    print('attempt in session')
    return redirect('/')

def delete_session(request):
    del request.session['attempt']
    return redirect('/')