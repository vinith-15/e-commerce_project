from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import User

class CustomUserForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter User Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control','placeholder': 'Enter Email Address'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Enter Your Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Enter Confirm Password'}))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','placeholder': 'Enter Address','rows':3}))
    pincode = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Enter Pincode'}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'address', 'pincode']
