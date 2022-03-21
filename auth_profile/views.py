# from django.shortcuts import render
# from allauth.account.views import SignupView, LoginView


# Create your views here.


# def home(request):
#     template = 'index.html'
#     return render(request, template_name=template)


# class auth_login(LoginView):
#     template_name = 'login.html'

from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def login(request):
    return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')
