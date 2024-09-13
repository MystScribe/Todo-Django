from django.urls import path
from . import views


app_name = 'accounts'


urlpatterns = [
    path('SignUp/', views.SignUpView, name='SignUp'),
    path('SignIn/', views.SignInView, name='SignIn'),
    path('SignOut/', views.SignOutView, name='SignOut'),
]