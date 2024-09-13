from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserSignInForm, UserSignUpForm

def SignUpView(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = User.objects.create_user(username=cd['Username'], email=cd['Email'], password=cd['Password'])
            user.first_name = cd['FirstName']
            user.last_name = cd['LastName']
            user.save()
            messages.success(request, 'User Signed up successfully', 'success')
            return redirect('Todo:Todo')
    else:
        form = UserSignUpForm()
    return render(request, 'accounts/SignUp.html', {'form': form})

def SignInView(request):
    if request.method == 'POST':
        form = UserSignInForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['Username'], password=cd['Password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'User Signed in successfully', 'success')
                return redirect('Todo:Todo')
            else:
                messages.error(request, 'Username or Password wrong', 'danger')
    else:
        form = UserSignInForm()
    return render(request, 'accounts/SignIn.html', {'form': form})

def SignOutView(request):
    logout(request)
    messages.success(request, 'User Signed out successfully', 'success')
    return redirect('Todo:Todo')


