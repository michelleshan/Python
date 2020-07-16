from django.shortcuts import render, HttpResponse, redirect

def firstFunction(request):
    return HttpResponse("I've made my first function work!")

def secondFunction(request):
    return HttpResponse("Here's my second route")

def hello(request,name):
    return HttpResponse("Hello "+name)

def template(request):
    if 'msg' not in request.session:
        request.session['msg'] = ""
    context = {
        'name':'Sally',
        'numbers': [5,7,8]
    }
    return render(request,"index.html", context)

def submitForm(request):
    if request.method == 'POST': 
        print(request.POST)
        print(request.POST['message'])
        print(request.session['msg'])
        request.session['msg'] += request.POST['message']
    return redirect('/template')