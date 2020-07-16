from django.shortcuts import render, redirect
from .models import User, Quote
from django.contrib import messages
import re
import bcrypt
from django.db.models import Count
from datetime import datetime

def index(request):
    return render(request, "index.html")

def createUser(request):
    if request.method == "POST":
        errors = User.objects.create_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            print("User's password entered was " + request.POST['password'])
            hashed_pw = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
            user = User.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],email=request.POST['email'],date_of_birth=request.POST['dob'], password=hashed_pw)
            print("User's password has been changed to " + user.password)
            print("User's First Name:" + user.first_name)
            print("User's Last Name:" + user.last_name)
            print("User's Email:" + user.email)
            print("Date of Birth: " + user.date_of_birth)
    return redirect('/')

def login(request):
    if request.method == "POST":
        users_with_email = User.objects.filter(email=request.POST['email'])
        if users_with_email:
            user = users_with_email[0]                    
            if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
                request.session['user_id'] = user.id #IMPORTANT!!!
                return redirect('/home')
            else:
                print("Password didn't match")
                messages.error(request, "Incorrect name or password")
        else:
            print("Name not found")
            messages.error(request, "Incorrect name or password")
    return redirect('/')

def home(request):
    if request.method == "GET":
        if "user_id" in request.session:
            context = {
                "user": User.objects.get(id=request.session['user_id']),
                "allquotes": Quote.objects.annotate(likes=Count('users_who_liked')),
                "age": int((datetime.now().date() - (datetime.strptime(str(User.objects.get(id=request.session['user_id']).date_of_birth), "%Y-%m-%d").date())).days / 365),
            }
            return render(request, "home.html", context)
        else:
            return redirect('/')

def addQuote(request):
    if request.method == "POST":
        errors = Quote.objects.quote_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
        else:
            Quote.objects.create(author = request.POST['author'], quote = request.POST['quote'], uploaded_by = User.objects.get(id = request.session['user_id']))
            quoteadded = Quote.objects.get(author= request.POST['author'])
            quoteadded.users_who_liked.add(User.objects.get(id=request.session['user_id']))
    return redirect('/home')

def Like(request, id):
    if request.method == "POST":
        quotetolike= Quote.objects.filter(id=id)
        if quotetolike:
                quote = quotetolike[0]
                user = User.objects.get(id=request.session['user_id'])
                quote.users_who_liked.add(user)
    return redirect('/home')

def deleteQuote(request, id):
    if request.method == "POST":
        quoteToDelete = Quote.objects.filter(id=id)
        if quoteToDelete:
                quote = quoteToDelete[0]
                user = User.objects.get(id=request.session['user_id'])
                if quote.uploaded_by == user:
                    quote.delete()
    return redirect('/home')

def deleteQuote2(request, id):
    if request.method == "POST":
        quoteToDelete = Quote.objects.filter(id=id)
        if quoteToDelete:
                quote = quoteToDelete[0]
                user = User.objects.get(id=request.session['user_id'])
                if quote.uploaded_by == user:
                    quote.delete()
    return redirect('/userquotes/'+str(request.session['user_id']))

def Unlike(request, id):
    if request.method == "POST":
        quotetounlike= Quote.objects.filter(id=id)
        if quotetounlike:
                quote = quotetounlike[0]
                user = User.objects.get(id=request.session['user_id'])
                quote.users_who_liked.remove(user)
    return redirect('/home')

def MyAccount(request):
    if "user_id" in request.session:
        context = {
            "user": User.objects.get(id=request.session['user_id']),
            "age": int((datetime.now().date() - (datetime.strptime(str(User.objects.get(id=request.session['user_id']).date_of_birth), "%Y-%m-%d").date())).days / 365),
        }
        return render(request, 'myaccount.html', context)
    else:
        return redirect('/')

def UpdateAccount(request):
    update = User.objects.get(id=request.session['user_id'])
    if request.method == "POST":
        context = {
            "user": User.objects.get(id=request.session['user_id']),
            "age": int((datetime.now().date() - (datetime.strptime(str(User.objects.get(id=request.session['user_id']).date_of_birth), "%Y-%m-%d").date())).days / 365),
        }
        if len(request.POST['first_name']) < 3:
            messages.error(request,"First Name is too short")
        FNAME_REGEX = re.compile(r'^[a-zA-Z-]+$')
        if len(request.POST['first_name']) > 0:
            if not FNAME_REGEX.match(request.POST['first_name']):
                messages.error(request,"First Name must not contain numbers or especial characters")
        if len(request.POST['last_name']) < 3:
            messages.error(request,"Last Name is too short")
        LNAME_REGEX = re.compile(r'^[a-zA-Z-]+$')
        if len(request.POST['last_name']) > 0:
            if not LNAME_REGEX.match(request.POST['last_name']):
                messages.error(request,"Last Name must not contain numbers or especial characters")
        if len(request.POST['email'])< 5:
            messages.error(request,"Email too short")
        users_with_email_dup = User.objects.filter(email=request.POST['email'])
        if len(users_with_email_dup) > 0 and users_with_email_dup[0] != User.objects.get(id=request.session['user_id']):
            messages.error(request,"Email already in use in another account")
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(request.POST['email']) > 0:                                         
            if not EMAIL_REGEX.match(request.POST['email']):
                messages.error(request,"Email is not in correct format")
        if len(request.POST['dob']) <8:
            messages.error(request,"Enter a valid Date")
        else:
            date1 = datetime.strptime(request.POST['dob'], "%Y-%m-%d").date()
            if date1 >= datetime.now().date():
                messages.error(request,"Birth Date must be in the Past") 
            age = int((datetime.now().date() - date1).days / 365)
            print(age)
            if age<13:
                messages.error(request,"You Should be at least 13 years old to continue (COPPA Compliant)")
            else:
                update.first_name = request.POST['first_name']
                update.last_name = request.POST['last_name']
                update.email = request.POST['email']
                update.date_of_birth = request.POST['dob']
                update.save()
        return redirect('/myaccount')

def UserQuotes(request, id):
        context = {
            "user": User.objects.get(id=request.session['user_id']),
            "age": int((datetime.now().date() - (datetime.strptime(str(User.objects.get(id=request.session['user_id']).date_of_birth), "%Y-%m-%d").date())).days / 365),
            "userquotes": User.objects.get(id=id),
        }
        return render(request, "quotes.html", context)

def logout(request):
    if request.method == "POST":
        request.session.clear()
    return redirect('/')