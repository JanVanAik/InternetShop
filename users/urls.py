from django.urls import path
from users.views import users, register

app_name = "users"

urlpatterns = [
    path('', users, name='user'),
    path('register/', register, name='register'),
]
