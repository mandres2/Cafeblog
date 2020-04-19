from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    # The Meta class gives a nested name space for configurations and keeps it all in one place for a targeted model. So in this case it will be the user model.
    class Meta:
        #Specify the model the form to interact with
        model = User
        # fields to be shown in form
        fields = ['username', 'email', 'password1', 'password2']


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
        class Meta:
            model = Profile
            fields = ['image']