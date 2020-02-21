from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # class Meta is a nested namespace for the configuration and keeps them in one place
    class Meta:
        # within the config, the model affected is the User model
        model = User
        # fields in the list are the fields that we want on the form and are in that specific order
        fields = [ 'username', 'email', 'password1', 'password2']