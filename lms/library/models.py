from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta


class Book(models.Model):

    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
        ]
    name = models.CharField(max_length=30)
    isbn = models.PositiveIntegerField()
    author = models.CharField(max_length=40)
    category = models.CharField(max_length=30, choices=catchoice, default='education')

    def __str__(self):
        return str(self.name)+"["+str(self.isbn)+']'


def get_expiry():
    return datetime.today() + timedelta(days=15)


class IssuedBook(models.Model):

    enrollment = models.CharField(max_length=30)

    isbn = models.CharField(max_length=30)

    issuedate = models.DateField(auto_now=True)

    expirydate = models.DateField(default=get_expiry)

    def __str__(self):
        return self.enrollment
