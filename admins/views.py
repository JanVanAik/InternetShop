from django.shortcuts import render

# Create your views here.
def admin_index(request):
    context = {
        'title': "GeekShop-ADMIN PANEL"
    }
    return render(request, 'admins/admin-index.html', context)

def admin_create(request):
    context = {
        'title': "GeekShop-CREATE"
    }
    return render(request, 'admins/admin-users-create.html', context)


def admin_read(request):
    context = {
        'title': "GeekShop-READ"
    }
    return render(request, 'admins/admin-users-read.html', context)


def admin_update(request):
    context = {
        'title': "GeekShop-UPDATE"
    }
    return render(request, 'admins/admin-users-update-delete.html', context)
