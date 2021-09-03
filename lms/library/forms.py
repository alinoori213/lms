from django import forms
from django.contrib.auth.models import User
from .models import *
from account.models import *


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'isbn', 'author', 'category']


class IssuedBookForm(forms.Form):

    isbn2 = forms.ModelChoiceField(queryset=Book.objects.all(),
                                   empty_label="Name and isbn",
                                   to_field_name="isbn", label='Name and Isbn')
    enrollment2 = forms.ModelChoiceField(queryset=CustomUser.objects.all(),
                                         )

