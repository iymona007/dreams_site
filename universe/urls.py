from django.urls import path

from . import views

urlpatterns = [
    path('mission/', views.mission, name='mission'),
    path('bottles/', views.bottle_list, name='bottle_list'),
    path('bottles/new/', views.bottle_create, name='bottle_create'),
    path('bottles/<int:pk>/', views.bottle_detail, name='bottle_detail'),
]
