from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect



def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'core/sign_up.html', {'form': form})



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        raw_password = request.POST['password']
        user = authenticate(username=username, password=raw_password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully !!')
            return redirect('home')
    else:
        return render(request, 'core/login.html')


def home(request):
    context = {'home' : 'active'}
    if request.user.is_authenticated:
        return render(request, 'core/home.html', context)
    else:
        return HttpResponseRedirect('/login/')


def contact(request):
    context = {'contact':'active'}
    if request.user.is_authenticated:
        return render(request, 'core/contact.html', context)
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request): 
    logout(request)
    return render(request, 'core/home.html')

