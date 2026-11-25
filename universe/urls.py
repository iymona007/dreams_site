from django.urls import path
from . import views

urlpatterns = [
    path('', views.mission, name='home'),
    path('mission/', views.mission, name='mission'),
    path('register/', views.register, name='register'),
    path('bottles/', views.bottle_list, name='bottle_list'),
    path('bottles/new/', views.bottle_create, name='bottle_create'),
    path('bottles/<int:pk>/', views.bottle_detail, name='bottle_detail'),
    path('profile/<str:username>/', views.profile, name='profile'),
]