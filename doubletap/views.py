from django.contrib.auth import authenticate, login
from django.http import request
from doubletap.forms import SignUpForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def index(request):
    return render(request,'index.html')


def register(request):
    if request.method=="POST":
        form=SignUpForm(request.POST)
        
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           user_password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=user_password)
           login(request, user)
        return redirect('login')
    else:
        form= SignUpForm()
    return render(request, 'registration/registration_form.html', {"form":form})        