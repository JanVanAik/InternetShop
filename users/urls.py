from django.urls import path
from users.views import  logout, verify, UserRegistrationForm, UserProfileForm, UserLoginForm

app_name = "users"

urlpatterns = [
    path('', UserLoginForm.as_view(), name='user'), #login
    path('register/', UserRegistrationForm.as_view(), name='register'),
    path('logout/', logout, name='logout'),
    path('profile/<int:pk>/', UserProfileForm.as_view(), name='profile'),


    path('verify/<str:email>/<str:activate_key>', verify, name='verification'),


]
