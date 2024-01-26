from django.shortcuts import render

# Create your views here.


def users(request):
    context = {
        "title": "Пользователь"
    }
    return render(request, 'users/login.html', context)


def register(request):
    context = {
        "title": "Регистрация"
    }
    return render(request, 'users/register.html', context)