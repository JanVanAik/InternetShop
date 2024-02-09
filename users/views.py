from django.contrib.auth.views import LoginView
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render, HttpResponseRedirect
from django.views.generic import CreateView, UpdateView

from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
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


class UserLoginForm(TitleMixin, LoginView):
    redirect_authenticated_user = True
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Авторизация пользователя'

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


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


class UserProfileForm(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    title = 'Профиль пользователя'
    template_name = 'users/profile.html'


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse("index"))


def verify(request, email, activate_key):
    try:
        user = User.objects.get(email=email)
        if user and user.activation_key == activate_key and not user.is_activation_key_expired:
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
