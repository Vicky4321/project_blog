from django.contrib import admin
from django.urls import path, include
from .import views


app_name='blog'
urlpatterns = [
    path('',views.BlogsListView.as_view(),name = 'index'),
]
