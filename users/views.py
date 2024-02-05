from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from basket.models import Basket
from users.models import User
from django.urls import reverse, reverse_lazy
from django.contrib import auth, messages
# Create your views here.


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['form'] = self.form_class()
        return context


class UserRegistrationForm(TitleMixin, CreateView):
    title = 'Регистрация пользователя'
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy("users:user")
    success_message = 'Пользователь успешно создан'

    def send_verify_link(self, user):
        verify_link = reverse('users:verification', args=[user.email, user.activation_key])
        subject = 'АКТИВАЦИЯ ПОЛЬЗОВАТЕЛЯ'
        message = f'Активируйте пользователя {user.username} пройдя по ссылке {settings.DOMAIN_NAME}{verify_link}'
        return send_mail(subject, message, settings.EMAIL_HOST_USER, fail_silently=False, recipient_list=[user.email])

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save()
            self.send_verify_link(user)
            return HttpResponseRedirect(reverse('users:user'))
        else:
            return super().get(request, *args, **kwargs)



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


# def register(request):
#
#     def send_verify_link(user):
#         verify_link = reverse('users:verification', args=[user.email, user.activation_key])
#         subject = 'АКТИВАЦИЯ ПОЛЬЗОВАТЕЛЯ'
#         message = f'Активируйте пользователя {user.username} пройдя по ссылке {settings.DOMAIN_NAME}{verify_link}'
#         return send_mail(subject, message, settings.EMAIL_HOST_USER, fail_silently=False, recipient_list=[user.email])
#
#
#     if request.method == "POST":
#         form = UserRegistrationForm(data=request.POST)
#         if form.is_valid():
#             user = form.save()
#             send_verify_link(user)
#             messages.success(request, "Проверяй почту, братишка")
#             return HttpResponseRedirect(reverse("users:user"))
#         else:
#             print(form.errors)
#     else:
#         form = UserRegistrationForm()
#     context = {
#         "title": "Регистрация", "form": form
#     }
#     return render(request, 'users/register.html', context)


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
        user = User.objects.get(email=email)
        if user and user.activation_key == activate_key:
            user.activation_key = ''
            user.activation_key_expires = None
            user.is_active = True
            user.save(update_fields=['activation_key', 'activation_key_expires', 'is_active'])
            auth.login(request, user)
            return render(request, 'users/verification.html')
    except Exception as e:
        pass
    else:
        return render(request, 'users/verification.html')
