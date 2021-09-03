from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import *
from .forms import *
from django.http import HttpResponseRedirect
from django.contrib.auth.models import Group
from django.contrib import auth
from django.contrib.auth.decorators import login_required, user_passes_test
from datetime import datetime, timedelta, date

@login_required
def viewbook_view(request):
    books = Book.objects.all()
    return render(request,'library/viewbook.html', {'books':books})

@login_required
def issuebook_view(request):
    form = IssuedBookForm()
    if request.method == 'POST':

        form = IssuedBookForm(request.POST)
        if form.is_valid():
            obj = IssuedBook()
            obj.enrollment = request.POST.get('enrollment2')
            obj.isbn = request.POST.get('isbn2')
            obj.save()
            return render(request, 'library/bookissued.html')
    return render(request, 'library/issuebook.html', {'form': form})

@login_required
def viewissuedbook_view(request):
    issuedbooks = IssuedBook.objects.all()
    li = []
    for ib in issuedbooks:
        issdate = str(ib.issuedate.day)+'-'+str(ib.issuedate.month)+'-'+str(ib.issuedate.year)
        expdate = str(ib.expirydate.day)+'-'+str(ib.expirydate.month)+'-'+str(ib.expirydate.year)

        days = (date.today()-ib.issuedate)
        print(date.today())
        d = days.days
        fine = 0
        if d > 15:
            day = d - 15
            fine = day * 10

        books = list(Book.objects.filter(isbn=ib.isbn))
        students = list(CustomUser.objects.filter())
        i = 0
        for l in books:
            t = (students[i], books[i].name,)
            i = i + 1
            li.append(t)

    return render(request, 'library/viewissuedbook.html', {'li': li})

@login_required
def viewissuedbookbystudent(request):

    return render(request, 'library/viewissuedbookbystudent.html')
    # student = CustomUser.objects.filter(user_id=request.user.id)
    # issuedbook = IssuedBook.objects.filter(enrollment=student[0].enrollment)
    #
    # li1=[]
    #
    # li2=[]
    # for ib in issuedbook:
    #     books = Book.objects.filter(isbn=ib.isbn)
    #     for book in books:
    #         t = (request.user, student[0].enrollment, student[0].branch, book.name, book.author)
    #         li1.append(t)
    #
    #     issdate = str(ib.issuedate.day) + '-'+ str (ib.issuedate.month) +'-' + str(ib.issuedate.year)
    #
    #     expdate = str(ib.expirydate.day) +'-' + str(ib.expirydate.month) + '-'+ str(ib.expirydate.year)
    #
    #     days = (date.today()-ib.issuedate)
    #     print(date.today())
    #     d = days.days
    #     fine = 0
    #     if d > 15:
    #         day = d-15
    #         fine = day*10
    #     t = (issdate, expdate, fine)
    #     li2.append(t)
    #
    # return render(request, 'library/viewissuedbookbystudent.html', {'li1': li1, 'li2': li2})