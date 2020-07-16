from django.shortcuts import render, redirect, HttpResponse
from .models import Dungeon, Prisoner

def firstFunction(request):
    context = {
        "dungeons" : Dungeon.objects.all(),
        "prisoners" : Prisoner.objects.all()
    }
    return render(request,'index.html',context)

def register_dungeon(request):
    Dungeon.objects.create(name=request.POST['name'],location=request.POST['location'],num_people_inside=request.POST['prisoners'])
    return redirect('/')

def register_prisoner(request):
    Prisoner.objects.create(name=request.POST['name'],dungeon_inside=Dungeon.objects.get(id=request.POST['dungeon_inside']))
    return redirect('/')

def delete(request,id):
    Dungeon.objects.get(id=id).delete()
    return redirect('/')