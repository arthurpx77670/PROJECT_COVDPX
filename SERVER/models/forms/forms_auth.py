from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class loginForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class EditForm(forms.Form):
    username = forms.CharField(max_length=30, required=False)
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=30, required=False)
    picture = forms.ImageField(required=False)


class ForgetPswForm(forms.Form):
    username = forms.CharField(label="Nom d'utilisateur", max_length=30)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')


class RebootPswForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('password1', 'password2')