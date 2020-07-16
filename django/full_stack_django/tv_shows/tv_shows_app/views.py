from django.shortcuts import render, redirect, HttpResponse
from .models import Show
from django.contrib import messages

def index(request):
    context = {
        'shows': Show.objects.all()
    }
    return render(request,'index.html',context)

def add_show(request):
    return render(request,'add_show.html')

def shows_create(request):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/shows/new')
    else:
        some_show = Show.objects.create(
        title=request.POST['title'],
        network=request.POST['network'],
        release_date=request.POST['release_date'],
        description=request.POST['description'])
        return redirect("/shows/"+str(some_show.id))

def show_info(request,id):
    context = {
        'some_show' : Show.objects.get(id=id)
    }
    return render(request,'show_info.html',context)

def edit_show(request,id):
    context = {
        'some_show2':Show.objects.get(id=id)
    }
    return render(request,'edit_show.html',context)

def shows_update(request,id):
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
            return redirect('/shows/'+str(id)+'/edit')
    else:
        this_show = Show.objects.get(id=id)
        this_show.title=request.POST['title']
        this_show.network=request.POST['network']
        this_show.release_date=request.POST['release_date']
        this_show.description=request.POST['description']
        this_show.save()
        return redirect('/shows/'+str(this_show.id))

def delete_show(request,id):
    Show.objects.get(id=id).delete()
    return redirect('/shows')