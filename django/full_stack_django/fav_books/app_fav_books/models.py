from django.db import models
import re

class UserManager(models.Manager):
    def create_validator(self,requestPOST):
        errors={}
        if len(requestPOST['first_name']) < 2 or len(requestPOST['last_name']) < 2:
            errors['name_too_short'] = "Both first and last name must be at least 2 characters."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(requestPOST['email']):          
            errors['invalid_email'] = "Invalid email address!"
        existing_emails = User.objects.filter(email=requestPOST['email'])
        if len(existing_emails) > 0:
            errors['dup_email'] = "This email already belongs to a registered user."
        if len(requestPOST['password']) < 8:
            errors['password_too_short'] = "Password must be at least 8 characters."
        if requestPOST['password_confirm'] != requestPOST['password']:
            errors['password_confirm'] = "Password confirmation does not match Password."
        return errors
    def login_validator(self,requestPOST):
        errors={}
        existing_emails = User.objects.filter(email=requestPOST['email'])
        if len(existing_emails) < 1:
            errors['unregistered_email'] = "This email address does not belong to a registered user."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class BookManager(models.Manager):
    def create_validator(self,requestPOST):
        errors={}
        if len(requestPOST['title']) < 1:
            errors['title_required'] = "Title is a required field."
        if len(requestPOST['desc']) < 5:
            errors['desc_too_short'] = "Description must be at least 5 characters."
        existing_books = Book.objects.filter(title=requestPOST['title'])
        if len(existing_books) > 0:
            errors['dup_book'] = "A book with this title already exists."
        return errors
    def edit_validator(self,requestPOST):
        errors={}
        if len(requestPOST['new_title']) < 1:
            errors['title_required'] = "Title is a required field."
        if len(requestPOST['new_desc']) < 5:
            errors['desc_too_short'] = "Description must be at least 5 characters."
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField()
    added_by = models.ForeignKey(User,related_name='books_added',on_delete=models.CASCADE)
    fav_by = models.ManyToManyField(User,related_name='fav_books')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = BookManager()