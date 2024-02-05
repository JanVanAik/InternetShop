from django.urls import path
from users.views import users, logout, profile, verify, UserRegistrationForm


app_name = "users"

urlpatterns = [
    path('', users, name='user'), #login
    path('register/', UserRegistrationForm.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('profile/', profile, name='profile'),


    path('verify/<str:email>/<str:activate_key>', verify, name='verification'),


]
