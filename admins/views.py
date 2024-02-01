from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from users.models import User
from admins.forms import UserAdminRegistrationForm

# Create your views here.
def admin_index(request):
    context = {
        'title': "GeekShop-ADMIN PANEL"
    }
    return render(request, 'admins/admin-index.html', context)

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


def admin_read(request):
    users = User.objects.all()
    context = {
        'title': "GeekShop-READ",
        'users': users
    }
    return render(request, 'admins/admin-users-read.html', context)


def admin_update(request):
    context = {
        'title': "GeekShop-UPDATE"
    }
    return render(request, 'admins/admin-users-update-delete.html', context)
