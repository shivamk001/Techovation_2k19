from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.
class HomePageView(TemplateView):
    template_name='account/home.html'
class EventView(TemplateView):
    template_name='account/event.html'
