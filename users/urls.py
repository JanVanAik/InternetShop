from django.urls import path
from users.views import users, register, logout, profile, verify


app_name = "users"

urlpatterns = [
    path('', users, name='user'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),


    path('verify/<str:email>/<str:activation_key>', verify, name='verification'),


]
