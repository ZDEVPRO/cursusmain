from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.forms import TextInput, EmailInput, FileInput, Select
from user.models import UserProfile

class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=255, label='Username')
    email = forms.CharField(max_length=255, label='Email')
    first_name = forms.CharField(max_length=255, label='Firstname')
    last_name = forms.CharField(max_length=255, label='Lastname')


    class Meta:
        model=User
        fields = ('username', 'email', 'first_name', 'last_name')

class UserUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')
        widgets = {
            'username'  :    TextInput(attrs={'class': 'input', 'placeholder':'Username'}),
            'email'     :    EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'first_name':    TextInput(attrs={'class': 'input', 'placeholder': 'Firstname'}),
            'last_name' :    TextInput(attrs={'class': 'input', 'placeholder': 'Lastname'}),

        }

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model=UserProfile
        fields=('phone', 'address', 'city', 'country', 'image')
        widgets = {
            'phone': TextInput(attrs={'class': 'input', 'placeholder':'Phone'}),
            'address': TextInput(attrs={'class': 'input', 'placeholder': 'Address'}),
            'city': TextInput(attrs={'class': 'input', 'placeholder': 'city'}),
            'country': TextInput(attrs={'class': 'input', 'placeholder': 'Country'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'image'}),
        }
