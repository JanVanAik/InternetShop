from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import user_passes_test
from django.utils.decorators import method_decorator
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


class DispatchMixin:

    @method_decorator(user_passes_test(lambda u: u.is_staff))
    def dispatch(self, request, *args, **kwargs):
        return super(DispatchMixin, self).dispatch(request, *args, **kwargs)


class TitleMixin:
    title = None

    def get_context_data(self, **kwargs):
        context = super(TitleMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context

class CommonMixin(DispatchMixin, TitleMixin):
    pass


class UserAdminListView(CommonMixin, ListView):
    model = User
    template_name = 'admins/admin-users-read.html'
    title = 'CustomAdminPanel'




class UserAdminUpdateView(CommonMixin, UpdateView):
    model = User
    form_class = UserAdminProfileForm
    title = 'Admin - UpdateUser'
    template_name = 'admins/admin-users-update-delete.html'


class UserAdminCreateView(CommonMixin, SuccessMessageMixin, CreateView):
    model = User
    title = 'Admin - CreateUser'
    form_class = UserAdminRegistrationForm
    template_name = 'admins/admin-users-create.html'
    success_url = reverse_lazy("admins:admins-read")
    success_message = 'Пользователь успешно создан'


class UserAdminDeleteView(DispatchMixin, DeleteView):
    model = User
    template_name = 'admins/admin-users-update-delete.html'
    success_url = reverse_lazy('admins:admins-read')


    def form_valid(self, form):
        self.object = self.get_object()
        self.object.safe_delete()
        return HttpResponseRedirect(self.success_url)



#
# Create your views here.
@user_passes_test(lambda u: u.is_staff)
def admin_index(request):
    context = {
        'title': "GeekShop-ADMIN PANEL"
    }
    return render(request, 'admins/admin-index.html', context)


# @user_passes_test(lambda u: u.is_staff)
# def admin_create(request):
#     if request.method == "POST":
#         form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("admins:admins-read"))
#     else:
#         form = UserAdminRegistrationForm()
#     context = {
#         'title': "GeekShop-CREATE",
#         "form": form
#     }
#     return render(request, 'admins/admin-users-create.html', context)
#
#
# @user_passes_test(lambda u: u.is_staff)
# def admin_read(request):
#     users = User.objects.all()
#     context = {
#         'title': "GeekShop-READ",
#         'users': users
#     }
#     return render(request, 'admins/admin-users-read.html', context)
#
#
# @user_passes_test(lambda u: u.is_staff)
# def admin_update(request, pk):
#     selected_user = User.objects.get(id=pk)
#     if request.method == "POST":
#         form = UserAdminProfileForm(instance=selected_user, data=request.POST, files=request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse("admins:admins-read"))
#     else:
#         form = UserAdminProfileForm(instance=selected_user)
#     context = {
#         'title': "GeekShop-UPDATE",
#         "form": form,
#         "selected_user": selected_user
#     }
#     return render(request, 'admins/admin-users-update-delete.html', context)
#
#
# def admin_delete(request, pk):
#     selected_user = User.objects.get(id=pk)
#     selected_user.delete()
#     return HttpResponseRedirect(reverse('admins:admins-read'))
