from .views import viewbook_view, issuebook_view, viewissuedbook_view, viewissuedbookbystudent
from django.urls import path


app_name = 'library'

urlpatterns = [

    path('', viewbook_view, name='login_form'),
    path('issuebook/', issuebook_view, name='issuebook'),
    path('viewissuedbook/', viewissuedbook_view, name='viewissuedbook'),
    path('viewissuedbookbystudent/', viewissuedbookbystudent, name='viewissuedbookbystudent'),


]
