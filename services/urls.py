from django.urls import path, include
from . import views
from django.shortcuts import render

app_name = 'services'

urlpatterns = [
    path('', views.shop, name='shop'),
]
