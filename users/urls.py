from django.urls import path
from users.views import users, register, logout, profile

app_name = "users"

urlpatterns = [
    path('', users, name='user'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),
]
