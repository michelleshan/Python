from __future__ import unicode_literals
from django.db import models
from datetime import datetime, date, time
import re

class ShowManager(models.Manager):
    def basic_validator(self,postData):
        errors={}
        if len(postData['title']) < 2:
            errors['title'] = "Title should be at least 2 characters."
        if len(postData['network']) < 3:
            errors['network'] = "Network should be at least 3 characters."
        x = postData['release_date']
        y = datetime.strptime(x,'%Y-%m-%d').date()
        print(datetime.now().date())
        if y >= datetime.now().date():
            errors['release_date'] = "Release date must be in the past"
        if len(postData['description']) >=1 and len(postData['description']) < 10:
            errors['description'] = "If adding a description, it should be at least 10 characters."
        show_title = Show.objects.filter(title=postData['title'])
        if len(show_title) > 0:
            errors['dup_show'] = "This TV show is already in the database."
        return errors

class Show(models.Model):
    title = models.CharField(max_length=255)
    network = models.CharField(max_length=45)
    release_date = models.DateTimeField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ShowManager()