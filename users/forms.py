# Import necessary modules
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from shopping.models import Profile
from django.contrib.auth.models import User

# Define SignUpForm class
class SignUpForm(UserCreationForm):
    """
    A form for user registration.

    Inherits from UserCreationForm, which is a built-in form provided by Django for user registration.
    Adds an email field to the form.

    Attributes:
        email (EmailField): The email field for the user's email address.

    Meta:
        model (User): The User model to be used for the form.
        fields (tuple): The fields to be included in the form.
    """

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')
    
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

# Define EditProfileForm class
class EditProfileForm(UserChangeForm):
    """
    A form for editing user profile.

    Inherits from UserChangeForm, which is a built-in form provided by Django for editing user profile.
    Adds additional fields to the form for editing user profile information.

    Attributes:
        email (EmailField): The email field for the user's email address.
        first_name (CharField): The field for the user's first name.
        last_name (CharField): The field for the user's last name.
        username (CharField): The field for the user's username.
        last_login (CharField): The field for the user's last login timestamp.
        is_superuser (CharField): The field for the user's superuser status.
        is_staff (CharField): The field for the user's staff status.
        is_active (CharField): The field for the user's active status.
        date_joined (CharField): The field for the user's join date.

    Meta:
        model (User): The User model to be used for the form.
        fields (list): The fields to be included in the form.
    """

    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    first_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_login = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    is_superuser = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_staff = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    is_active = forms.CharField(max_length=50, widget=forms.CheckboxInput(attrs={'class': 'form-check'}))
    date_joined = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'last_login', 'is_superuser', 'is_staff', 'is_active', 'date_joined']

# Define ProfilePageForm class
class ProfilePageForm(forms.ModelForm):
    """
    A form for editing user profile page.

    Inherits from ModelForm, which is a built-in form provided by Django for working with models.
    Adds additional fields to the form for editing user profile page information.

    Attributes:
        first_name (CharField): The field for the user's first name.
        last_name (CharField): The field for the user's last name.
        bio (Textarea): The field for the user's bio.
        profile_pic (ImageField): The field for the user's profile picture.
        venmo_url (CharField): The field for the user's Venmo URL.
        pinterest_url (CharField): The field for the user's Pinterest URL.

    Meta:
        model (Profile): The Profile model to be used for the form.
        fields (list): The fields to be included in the form.
        widgets (dict): The widgets to be used for each field.
    """

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'bio', 'profile_pic', 'venmo_url', 'pinterest_url']
        widgets = {
            'bio': forms.Textarea(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            # 'profile_pic': forms.ImageField(attrs={'class': 'form-control'}),
            'venmo_url': forms.TextInput(attrs={'class': 'form-control'}),
            'pinterest_url': forms.TextInput(attrs={'class': 'form-control'}),
        }
