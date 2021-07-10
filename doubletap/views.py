from doubletap.models import Profile
from django.contrib.auth import authenticate, login
from django.http import request
from doubletap.forms import SignUpForm, UserProfileUpdateForm, UserprofileForm
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Create your views here.
    #mainpage
@login_required(login_url='/accounts/login/')
def index(request):
    profile = Profile.objects.all()
    return render(request,'index.html',{"profile":profile,})

    # registration function
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

    #user profile function    
@login_required(login_url='/accounts/login/')    
def insta_profile(request):
    if request.method == 'POST':
        user_profile_form = UserprofileForm(request.POST, request.FILES, instance=request.user)
        if  user_profile_form.is_valid():
            user_profile_form.save()
            return redirect('home')
    else:
        user_profile_form = UserprofileForm(instance=request.user)
        user_form = UserProfileUpdateForm(instance=request.user)
    return render(request, 'user_profile.html',{"user_profile_form": user_profile_form,"user_form":user_form})

    # update user profile function 
@login_required(login_url='/accounts/login/')  
def Update_insta_Profile(request):
    if request.method == 'POST':
        user_form = UserProfileUpdateForm(request.POST, instance=request.user)
        profile_form = UserprofileForm(request.POST, request.FILES, instance=request.user)
        if  profile_form.is_valid():
            user_form.save(commit=True)
            profile_form.save()
            return redirect('profile')
    else: 
        profile_form = UserprofileForm(instance=request.user)
        user_form = UserProfileUpdateForm(instance=request.user)
    return render(request, 'update_userprofile.html',{"user_form":user_form,"profile_form": profile_form})
         