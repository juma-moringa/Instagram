
from doubletap.models import Profile
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
#signform
class SignUpForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

#user profile form
class UserprofileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'profile_photo', 'bio']  

#update profile form
class UserProfileUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email']   
