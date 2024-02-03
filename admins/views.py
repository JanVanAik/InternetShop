from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from users.models import User
from admins.forms import UserAdminRegistrationForm, UserAdminProfileForm


# Create your views here.
@user_passes_test(lambda u: u.is_staff)
def admin_index(request):
    context = {
        'title': "GeekShop-ADMIN PANEL"
    }
    return render(request, 'admins/admin-index.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_create(request):
    if request.method == "POST":
        form = UserAdminRegistrationForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admins:admins-read"))
    else:
        form = UserAdminRegistrationForm()
    context = {
        'title': "GeekShop-CREATE",
        "form": form
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_read(request):
    users = User.objects.all()
    context = {
        'title': "GeekShop-READ",
        'users': users
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_staff)
def admin_update(request, pk):
    selected_user = User.objects.get(id=pk)
    if request.method == "POST":
        form = UserAdminProfileForm(instance=selected_user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("admins:admins-read"))
    else:
        form = UserAdminProfileForm(instance=selected_user)
    context = {
        'title': "GeekShop-UPDATE",
        "form": form,
        "selected_user": selected_user
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


def admin_delete(request, pk):
    selected_user = User.objects.get(id=pk)
    selected_user.delete()
    return HttpResponseRedirect(reverse('admins:admins-read'))