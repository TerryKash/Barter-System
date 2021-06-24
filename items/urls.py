from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='ItemsHome'),
    path("about", views.about, name='ItemsAbout'),

]