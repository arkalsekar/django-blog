from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.blogHome, name='blogHome'),
    path("post/<str:slug>", views.blogPost, name='blogPost'),


]
