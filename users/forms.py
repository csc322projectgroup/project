from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile


class UserRegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField()
    balance = forms.IntegerField()
    cart = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    total_spent = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    status = forms.CharField(widget=forms.HiddenInput(), initial='regular')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'address', 'balance', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    balance = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username', 'email', 'balance']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']
