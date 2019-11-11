from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    #homepageview.as_view()
    path('',views.HomePageView.as_view(),name='home'),
    path('home/',views.HomePageView.as_view(),name='home'),
    path('event/',views.EventView.as_view(),name='event'),
    path('register/', views.register, name='register'),
    #path('login/', auth_views.LoginView.as_view(), name='login'),
    path('login/', views.user_login,name='login'),#this login only logs in admin"""
    path('logout/',auth_views.LogoutView.as_view(),name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/edit/', views.edit, name='edit'),
    path('dashboard/add_non_tech',views.add_events_nontech, name='add_non_tech'),
    path('dashboard/add_tech',views.add_events_tech, name='add_tech'),
    path('dashboard/my_events',views.my_events,name='my_events'),
]
