from django.shortcuts import render, HttpResponseRedirect
from .form import SignUpForm
# Create your views here.
def home(request):
    context = {'home' : 'active'}
    return render(request, 'core/home.html', context)


def contact(request):
    context = {'contact':'active'}
    return render(request, 'core/contact.html', context)

def user_signup(request):
    form = SignUpForm
    return render(request, 'core/sign_up.html', {'form' :form})

def user_login(request):
    context = {'contact':'active'}
    return render(request, 'core/login.html', context)

def user_logout(request):
    return HttpResponseRedirect('/')

