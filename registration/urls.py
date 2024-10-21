from . import views
from django.urls import path
from registration.views import register

app_name = 'registration'

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]