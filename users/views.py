from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from basket.models import Basket
from users.models import User
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

    def send_verify_link(user):
        verify_link = reverse('users:verification', args=[user.email, user.activation.key])
        return send_mail(verify_link, settings.EMAIL_HOST_USER, [user.email, ], fail_silently=False)


    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            send_verify_link(user)
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



def verify(request, email, activate_key):
    try:
        user = User.objects.filter(email=email)
        if user and user.activation_key == activate_key and not user.activation_key_expires:
            user.activation_key = ''
            user.activation_key_expires = None
            user.is_active = True
            user.save(update_fields=['acrtivation_key', 'activation_key_expires', 'is_active'])
            auth.login(request, user)
            return render(request, 'user/verification.html')
    except Exception as e:
        pass
    else:
        return render(request, 'user/verification.html')
