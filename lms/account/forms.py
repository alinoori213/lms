from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class UserForm(forms.Form):

    types = forms.ChoiceField(choices=(('teacher', 'teacher'),
                                       ('student', 'student'),
                                       ('staff', 'staff'),))
    phone = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)