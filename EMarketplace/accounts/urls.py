from django.urls import path
from . import views

urlpatterns = [
    path('', views.RegistrationView, name='register'),
    path('login/', views.LoginView, name='login'),
]
