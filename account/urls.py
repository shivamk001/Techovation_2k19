from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    #homepageview.as_view()
    path('home',views.HomePageView.as_view(),name='home'),
]
