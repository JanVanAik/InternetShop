from django.urls import path
from admins.views import admin_index, admin_read, admin_create, admin_update

app_name = "admins"

urlpatterns = [
    path('', admin_index, name='index'),
    path('admin-users-create/', admin_create, name='admins-create'),
    path('admin-users-read/', admin_read, name='admins-read'),
    path('admin-users-update/', admin_update, name='admins-update')
]