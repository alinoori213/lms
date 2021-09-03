from django.contrib.auth import login
from django.shortcuts import render
from .forms import UserForm
from django.views import generic
from django.db.models import F
from django.views.generic.edit import FormView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def login_form(request):

    login_form = UserForm()
    if request.method == "POST":

        login_form = UserForm(request.POST)

        if login_form.is_valid():
            type = login_form['types']
            print(type)
            user = authenticate(phone=login_form.cleaned_data['phone'],
                                password=login_form.cleaned_data['password'])

            if user is not None:
                print(user)
                login(request, user)
                return redirect('/library')
                # return redirect(reverse_lazy('account'))
            else:
                return HttpResponseRedirect(request.path_info)

    else:
        return render(request, 'account/login.html', {"form": login_form})
