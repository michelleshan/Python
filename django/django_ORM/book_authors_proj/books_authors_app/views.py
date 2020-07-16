from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author

def main(request):
    return render(request,'main.html')

def books_index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request,'books_index.html',context)

def books(request,id):
    context = {
        'some_book': Book.objects.get(id=id),
        'authors' : Book.objects.get(id=id).books_authors.all(),
        'missing_author': Author.objects.all()
    }
    return render(request,'books.html',context)

def add_missing_author(request,id):
    Book.objects.get(id=id).books_authors.add(Author.objects.get(id=request.POST['author']))
    return redirect('/books/'+str(id))

def delete_author(request,id,author_id):
    Book.objects.get(id=id).books_authors.remove(Author.objects.get(id=author_id))
    return redirect('/books/'+str(id))

def add_books(request):
    Book.objects.create(title=request.POST['title'],desc=request.POST['description'])
    return redirect('/')

def return_main(request):
    return redirect('/books_index')

def authors_index(request):
    context={
        'authors': Author.objects.all()
    }
    return render(request,'authors_index.html',context)

def authors(request,id):
    context = {
        'some_author': Author.objects.get(id=id),
        'books': Author.objects.get(id=id).books_authors.all(),
        'missing_book': Book.objects.all()
    }
    return render(request,'authors.html',context)

def add_missing_book(request,id):
    Author.objects.get(id=id).books_authors.add(Book.objects.get(id=request.POST['book']))
    return redirect('/authors/'+str(id))

def add_authors(request):
    Author.objects.create(first_name=request.POST['first_name'],last_name=request.POST['last_name'],notes=request.POST['notes'])
    return redirect('/authors')

def return_authors_index(request):
    return redirect('/authors_index')

def delete_book(request,id,book_id):
    Author.objects.get(id=id).books_authors.remove(Book.objects.get(id=book_id))
    return redirect('/authors/'+str(id))