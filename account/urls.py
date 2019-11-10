from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    #homepageview.as_view()
    path('home',views.HomePageView.as_view(),name='home'),
    path('event',views.EventView.as_view(),name='event'),
    path('register/', views.register, name='register'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', views.user_login,name='login'),#this login only logs in admin"""
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/edit/', views.edit, name='edit'),
]
