from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms
from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput
        (attrs={'class': 'form-control py-4', "placeholder": "Введите имя пользователя"}))
    password = forms.CharField(widget=forms.PasswordInput
        (attrs={'class': 'form-control py-4', "placeholder": "Введите  пароль"}))

    class Meta:
        model = User
        fields = ("username", "password")


class UserRegistrationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput
        (attrs={'class': 'form-control py-4', "placeholder": "Введите имя пользователя"}))
    firstname = forms.CharField(widget=forms.TextInput
        (attrs={'class': 'form-control py-4', "placeholder": "Введите имя"}))
    lastname = forms.CharField(widget=forms.TextInput
        (attrs={"class": 'form-control py-4', "placeholder": "Введите фамилию"}))
    email = forms.CharField(widget=forms.EmailInput
        (attrs={'class': 'form-control py-4', "placegolder": "Введите адрес эл. почты"}))
    password1 = forms.CharField(widget=forms.PasswordInput
        (attrs={'class': 'form-control py-4', "placeholder": "Введите  пароль"}))
    password2 = forms.CharField(widget=forms.PasswordInput
        (attrs={'class': 'form-control py-4', "placeholder": "Введите  пароль"}))

    class Meta:
        model = User
        fields = ("username", "firstname", "lastname", "email", "password1", "password2")
