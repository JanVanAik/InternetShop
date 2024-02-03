from django.urls import path
from admins.views import UserAdminListView, UserAdminCreateView, UserAdminDeleteView, UserAdminUpdateView, admin_index

app_name = "admins"

urlpatterns = [
    path('', admin_index, name='index'),
    path('admin-users-create/', UserAdminCreateView.as_view(), name='admins-create'),
    path('admin-users-read/', UserAdminListView.as_view(), name='admins-read'),
    path('admin-users-update/<int:pk>/', UserAdminUpdateView.as_view(), name='admins-update'),
    path('admin-users-delete/<int:pk>/', UserAdminDeleteView.as_view(), name='admins-delete')
]