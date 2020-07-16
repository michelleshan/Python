from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt
from django.db.models import Count

def index(request):
    return render(request,'index.html')

def create_user(request):
    if request.method == 'POST':
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                print('UNsuccessful creation')
            return redirect('/')
        else:
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            some_user = User.objects.create(
                first_name=request.POST['first_name'],
                last_name=request.POST['last_name'],
                email=request.POST['email'],
                password=hashed_pw
            )
            request.session['user_id'] = some_user.id 
            print('successful creation!')
    return redirect('/books')

def login(request):
    if request.method == 'POST':
        existing_user = User.objects.filter(email=request.POST['email'])
        if existing_user:
            logged_user = existing_user[0]
            if bcrypt.checkpw(request.POST['password'].encode(),logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                print('login SUCCESSFUL!')
                return redirect('/books')
            else:
                messages.error(request,"Incorrect password")
                print('login UNsuccessful :(')
        else:
            errors = User.objects.login_validator(request.POST)
            print('email not registered')
            if len(errors) > 0:
                for key, value in errors.items():
                    messages.error(request,value)
    return redirect('/')

def home(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        context = {
            'some_user': User.objects.get(id=request.session['user_id']),
            'books': Book.objects.all(),
            'favorites': User.objects.get(id=request.session['user_id']).fav_books.all()
        }
    return render(request,'books.html',context)

def log_out(request):
    del request.session['user_id']
    return redirect('/')

def add_book(request):
    if request.method == "POST":
        errors = Book.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            some_user = User.objects.get(id=request.session['user_id'])
            some_book = Book.objects.create(
            title=request.POST['title'],
            desc=request.POST['desc'],
            added_by=User.objects.get(id=request.session['user_id'])
            )
            some_user.fav_books.add(some_book.id)
    return redirect('/books')

def add_favorite(request,id):
    some_book = Book.objects.get(id=id)
    User.objects.get(id=request.session['user_id']).fav_books.add(some_book.id)
    return redirect(f'/books/{id}')

def unfavorite(request,id):
    some_book = Book.objects.get(id=id)
    User.objects.get(id=request.session['user_id']).fav_books.remove(some_book.id)
    return redirect(f'/books/{id}')

def all(request):
    context = {
        'users': User.objects.all(),
        'books': Book.objects.all()
    }
    return render(request,'all.html',context)

def delete_user(request,id):
    User.objects.get(id=id).delete()
    return redirect('/all')

def delete_book(request,id):
    Book.objects.get(id=id).delete()
    return redirect('/books')

def some_book(request,id):
    if 'user_id' not in request.session:
        return redirect('/')
    user = Book.objects.get(id=id).added_by.id
    if (request.session['user_id'] != user):
        context = {
            'some_book' : Book.objects.get(id=id),
            'some_user' : User.objects.get(id=request.session['user_id']),
            'some_book_lovers' : Book.objects.get(id=id).fav_by.all()
        }
        print("Someone else's book")
        return render(request,'some_book.html',context)
    else:
        context = {
            'some_book' : Book.objects.get(id=id),
            'some_user' :User.objects.get(id=request.session['user_id']),
            'some_book_lovers' : Book.objects.get(id=id).fav_by.all()
        }
        print("My book")
        return render(request,'my_book.html',context)

def favorite_books(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'fav_books': user.fav_books.all()
    }
    return render(request,'fav_books.html',context)

def edit_book(request,id):
    if 'user_id' not in request.session:
        return redirect('/')
    if request.method == "POST":
        errors = Book.objects.edit_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
                return redirect(f'/books/{id}')
    some_book = Book.objects.get(id=id)
    if request.session['user_id'] == some_book.added_by.id:
        some_book.title=request.POST['new_title']
        some_book.desc=request.POST['new_desc']
        some_book.save()
        return redirect(f'/books/{id}')
    else:
        return redirect('/books')