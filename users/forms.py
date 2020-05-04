from django import forms
from django.contrib.auth.models import User
# this will create a new from the inherits from the user creation form
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

# Changing the user creation form
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        # model that we want this form to interact with here
        # whenever this form valides its going to create a new user
        # when the from is saved its going be saved to this user model
        model = User
        fields = ['username', 'email','password1','password2']
# user form will allow us to update username and email
class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email']

    
# profile form will allow us the update our image
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

