from django.urls import path
from admins.views import admin_index, admin_read, admin_create, admin_update, admin_delete

app_name = "admins"

urlpatterns = [
    path('', admin_index, name='index'),
    path('admin-users-create/', admin_create, name='admins-create'),
    path('admin-users-read/', admin_read, name='admins-read'),
    path('admin-users-update/<int:pk>/', admin_update, name='admins-update'),
    path('admin-users-delete/<int:pk>/', admin_delete, name='admins-delete')
]