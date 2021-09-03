from .views import login_form
from django.urls import path


app_name = 'account'

urlpatterns = [

    path('', login_form, name='login_form'),


]
