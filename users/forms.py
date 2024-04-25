from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User


# Create your models here.
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']

class EditProfileForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    bio = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    venmo_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    pinterest_url = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    profile_pic = forms.ImageField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'bio', 'venmo_url', 'pinterest_url', 'profile_pic']

