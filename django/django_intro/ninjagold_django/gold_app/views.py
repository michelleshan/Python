from django.shortcuts import render, redirect, HttpResponse
import random

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    if 'g' not in request.session:
        request.session['g'] = 0
    return render(request,'index.html')

def process(request):
    if request.POST['location'] == 'farm':
        request.session['g'] = random.randint(10,20)
        request.session['gold'] += request.session['g']
        request.session['activities'].append(f"You earned {request.session['g']} golds!")
    elif request.POST['location'] == 'cave':
        request.session['g'] = random.randint(5,10)
        request.session['gold'] += request.session['g']
        request.session['activities'].append(f"You earned {request.session['g']} golds!")
    elif request.POST['location'] =='house':
        request.session['g'] = random.randint(2,5)
        request.session['gold'] += request.session['g']
        request.session['activities'].append(f"You earned {request.session['g']} golds!")
    elif request.POST['location'] == 'casino':
        request.session['g'] = random.randint(-50,50)
        request.session['gold'] += request.session['g']
        if request.session['g'] > 0:
            request.session['activities'].append(f"You earned {request.session['g']} golds!")
        else:
            request.session['activities'].append(f"Ouch...you lost {request.session['g']} golds!")
    return redirect('/')

def delete(request):
    del request.session['gold']
    del request.session['activities']
    return redirect('/')