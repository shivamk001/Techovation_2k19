from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import Profile
from .forms import UserRegistrationForm

# Create your views here.
class HomePageView(TemplateView):
    template_name='account/home.html'

class EventView(TemplateView):
    template_name='account/event.html'

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            #create a new user object but avoid saving it stylesheet
            new_user = user_form.save(commit=False)
            #set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            #save the User object
            new_user.save()
            #create the user Profile
            Profile.objects.create(user=new_user)
            return render(request,
                        'account/register_done.html',
                        {'new_user':new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form':user_form})
