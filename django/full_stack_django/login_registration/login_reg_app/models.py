from __future__ import unicode_literals
from django.db import models
import re
from datetime import datetime

class UserManager(models.Manager):
    def create_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "The first name field requires at least 2 characters."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "The last name field requires at least 2 characters."
        if postData['birthday'] > dt.date.today():
            errors['birthday'] = "Birthday must be in the past."
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):          
            errors['email'] = "Invalid email address!"
        existing_emails = User.objects.filter(email=postData['email'])
        print(existing_emails)    
        if len(existing_emails) > 0:
            errors['dup_email'] = "This email already belongs to a registered user."
        if len(postData['password']) < 8:
            errors['password_length'] = "Your password must be at least 8 characters."
        if postData['password_confirm'] != postData['password']:
            errors['mismatch'] = "Password and Password Confirmation do not match."
        return errors
    def login_validator(self, postData):
        errors = {}
        existing_emails = User.objects.filter(email=postData['email'])
        if len(existing_emails) < 1:
            errors['no_email'] = "This email is not registered in the database."
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    birthday = models.DateField()
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()