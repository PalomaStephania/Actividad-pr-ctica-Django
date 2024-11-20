from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('home/', views.IndexView.as_view()),
]
