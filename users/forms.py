from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import BillingInformation

# Customised Login form 
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.PasswordInput(attrs={'class': 'form-control'})

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class PaymentForm(ModelForm):
    price = forms.CharField(required=False, label='Amount Due', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'id': 'price',
        'readonly': True,
        'value': 1
    }))

    class Meta:
        model = BillingInformation
        fields = ('email', 'phone', 'price', 'payment_method')
