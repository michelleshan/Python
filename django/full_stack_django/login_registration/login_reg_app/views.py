from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request,'index.html')

def create_user(request):
    if request.method == 'POST':
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/')
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(),bcrypt.gensalt()).decode()
            some_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_pw)
            request.session['user_id']=some_user.id
    return redirect('/success')

def login_user(request):
    if request.method == 'POST':
        some_user = User.objects.filter(email=request.POST['email'])
        if some_user:
            logged_user = some_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/success')
            else:
                messages.error(request,"Incorrect email or password.")
        errors = User.objects.login_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect('/')
    else:
        return redirect('/')
    return redirect('/success')

def success(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context = {
        'some_user': User.objects.get(id=request.session['user_id'])
        }
        return render(request,'success.html',context)


def all_users(request):
    context = {
        'users':User.objects.all()
    }
    return render(request,'allusers.html',context)

def delete_users(request,id):
    User.objects.get(id=id).delete()
    print("Hello "+str(id))
    return redirect('/allusers')

def destroy(request):
    del request.session['user_id']
    return redirect('/')