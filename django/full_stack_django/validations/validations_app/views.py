from django.shortcuts import render
from django.contrib import messages
from django.models import Blog, BlogManager

def update(request,id):
    errors = Blog.objects.basic_validators(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/blog/edit/'+id)
    else:
        # if the errors object is empty, that means there were no errors!
        # retrieve the blog to be updated, make the changes, and save
        blog = Blog.objects.get(id = id)
        blog.name = request.POST['name']
        blog.desc = request.POST['desc']
        blog.save()
        messages.success(request, "Blog successfully updated")
        # redirect to a success route
        return redirect('/blogs')