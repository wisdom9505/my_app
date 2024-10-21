from django.views.generic import ListView, DetailView
from .models import Post
from django.urls import path, include
from . import views

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
]