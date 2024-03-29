from django import forms

from users.forms import UserRegistrationForm, UserProfileForm
from users.models import User


class UserAdminRegistrationForm(UserRegistrationForm):
    image = forms.ImageField(widget=forms.FileInput
    (attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'image', 'email', 'password1', 'password2')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput
    (attrs={'class': 'form-control py-4', "placeholder": "Введите имя пользователя", "readonly": False}), )
    email = forms.CharField(widget=forms.EmailInput
    (attrs={'class': 'form-control py-4', "placegolder": "Введите адрес эл. почты", "readonly": False}))


    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "image")