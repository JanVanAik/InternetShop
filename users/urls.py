from django.urls import path
from users.views import users, register, logout

app_name = "users"

urlpatterns = [
    path('', users, name='user'),
    path('register/', register, name='register'),
    path('logout/', logout, name='logout'),
]
