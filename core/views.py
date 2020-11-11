from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm, LoginForm
from django.contrib import messages

# Create your views here.
def home(request):
    context = {'home' : 'active'}
    return render(request, 'core/home.html', context)


def contact(request):
    context = {'contact':'active'}
    return render(request, 'core/contact.html', context)

def user_signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation !! You have a become author.')
            form.save()
    else:
        form = SignUpForm
        return render(request, 'core/sign_up.html', {'form' :form})

def user_login(request):
    form = LoginForm()
    return render(request, 'core/login.html', {'form' :form})

def user_logout(request):
    return HttpResponseRedirect('/')

