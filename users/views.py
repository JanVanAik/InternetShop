from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from basket.models import Basket
from django.urls import reverse
from django.contrib import auth, messages
# Create your views here.


def users(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(reverse("index"))
    else:
        form = UserLoginForm()
    context = {
        "title": "Авторизация",
        'form': form
    }
    return render(request, 'users/login.html', context)


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "GzGz!!")
            return HttpResponseRedirect(reverse("users:user"))
        else:
            print(form.errors)
    else:
        form = UserRegistrationForm()
    context = {
        "title": "Регистрация", "form": form
    }
    return render(request, 'users/register.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))

def profile(request):
    if request.method == "POST":
        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("users:profile"))
    else:
        form = UserProfileForm(instance=request.user)
    context = {
        "title": "Профиль",
        "form": form,
        "baskets": Basket.objects.filter(User=request.user),
    }
    return render(request, 'users/profile.html', context)