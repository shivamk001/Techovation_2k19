from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from .models import Profile, Participation_Tech, Participation_NonTech, Event_Technical, Event_Non_Technical
from .forms import UserRegistrationForm, LoginForm, UserEditForm, AddEventsTech, AddEventsNonTech
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class HomePageView(TemplateView):
    template_name='account/home.html'

class EventView(TemplateView):
    template_name='account/event.html'

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            #user = form.save()
            #print("USERNAME:", user[0])
            #user.refresh_from_db()
            #username = form.cleaned_data.get('username')
            #user.profile.first_name = form.cleaned_data.get('first_name')
            #user.profile.last_name = form.cleaned_data.get('last_name')
            #user.profile.email = form.cleaned_data.get('email')
            #user.profile.phone = form.cleaned_data.get('phone_number')
            #user.profile.username = username
            #user.save()

            #raw_password = form.cleaned_data.get('password1')
            #user = authenticate(username=username, password=raw_password)
            #login(request, user)
            user = form.save()
            username = form.cleaned_data['username']
            f_name = form.cleaned_data['first_name']
            l_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_num = form.cleaned_data['phone_number']
            college_name=form.cleaned_data['college']
            new_user = Profile(user=user, f_name=f_name, l_name=l_name,email=email,phone=phone_num,college=college_name)
            new_user.save()
            raw_password = form.cleaned_data['password1']
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'account/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    #return HttpResponse('Authenticated Successfully!')
                    return redirect('dashboard')

                else:
                    return HttpResponse('Disabled account')

            else:
                return HttpResponse('Invalid Login')

    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form':form})

@login_required
def dashboard(request):
    profile_dictionary={}
    username = str(request.user.username)
    list_users = list(Profile.objects.all())
    for objts in list_users:
        if str(objts.user) == username:
            email = str(objts.email)
            f_name = str(objts.f_name)
            l_name = str(objts.l_name)
            phone_num = str(objts.phone)
            college = str(objts.college)
            year = str(objts.year)
            break

    profile_dictionary['username'] = str(request.user.username)
    profile_dictionary['email'] = str(request.user.email)
    profile_dictionary['f_name'] = f_name
    profile_dictionary['l_name'] = l_name
    profile_dictionary['phone'] = phone_num
    profile_dictionary['college'] = college
    profile_dictionary['year'] = year
    #print(profile_dictionary['username'])
    #print(profile_dictionary['email'])
    return render(request, 'account/dashboard.html',profile_dictionary)

@login_required
def edit(request):
    if request.method == 'POST':
        form = UserEditForm(request.POST)

        if form.is_valid():
            username = str(request.user.username)
            list_users = list(Profile.objects.all())
            for objts in list_users:
                if str(objts.user) == username:
                    object = objts
                    break

            if form.cleaned_data['first_name'] != '':
                object.f_name = form.cleaned_data['first_name']

            if form.cleaned_data['last_name'] != '':
                object.l_name = form.cleaned_data['last_name']

            '''
            if form.cleaned_data['email'] != '':
                object.email = form.cleaned_data['email']
            '''

            if form.cleaned_data['phone_number'] != '':
                object.phone = form.cleaned_data['phone_number']

            if form.cleaned_data['college_name'] != '':
                object.college = form.cleaned_data['college_name']


            object.save()

            return redirect('dashboard')
    else:
        form = UserEditForm()
    return render(request, 'account/edit.html', {'form':form})

@login_required
def add_events_tech(request):
    print('Add Tech Events0')
    print(request.method)
    if request.method == 'GET':
        print('Add Tech Events3')
        form = AddEventsTech()
    else:
        print(request.method)
        form = AddEventsTech(request.POST)
        print('Add Tech Events1')
        if form.is_valid():
            username = str(request.user.username)
            list_users = list(Profile.objects.all())
            for objts in list_users:
                if str(objts.user) == username:
                    object_user = objts
                    break
            print('Add Tech Events2')
            print(object_user.user)


            event_tech =form.cleaned_data['event_name_tech']
            list_events = list(Event_Technical.objects.all())
            for objts in list_events:
                if str(objts.event_name_tech) == event_tech:
                    object_event = objts
                    break
            print(object_event.event_name_tech)

            object = Participation_Tech(participant = object_user, event = object_event)
            print(object.participant.user)
            print(object.event.event_name_tech)
            object.save()

            return redirect('add_tech')

    return render(request, 'account/event_tech_add.html', {'form':form})

@login_required
def add_events_nontech(request):
    if request.method == 'POST':
        form = AddEventsNonTech(request.POST)

        if form.is_valid():
            username = str(request.user.username)
            list_users = list(Profile.objects.all())
            for objts in list_users:
                if str(objts.user) == username:
                    object_user = objts
                    break

            event_non_tech =form.cleaned_data['event']
            list_events = list(Event_Non_Technical.objects.all())
            for objts in list.events:
                if str(objts.event_name_tech) == event_tech:
                    object_event = objts
                    break

            object = Participation_NonTech(participant = object_user, event = object_event)
            object.save()

            return redirect('add_non_tech')

    else:
        form = AddEventsTech()
    return render(request, 'account/event_non_tech_add.html', {'form':form})

@login_required
def my_events(request):
    user_name =str(request.user.username)
    print(user_name)
    #technical
    list_ = list(Participation_Tech.objects.all())
    user_event_list_tech= []
    for objts in list_:
        if str(objts.participant.user) == user_name:
            user_event_list_tech.append(objts.event.event_name_tech)
    user_event_list_tech = set(user_event_list_tech)

    #non-Technical
    list_ = list(Participation_NonTech.objects.all())
    user_event_list_nontech = []
    for objts in list_:
        if str(objts.participant.user) == username:
            user_event_list_tech.append(objts.event.event_name_non_tech)
    user_event_list_nontech = set(user_event_list_nontech)

    event_dict = {'tech': user_event_list_tech, 'non_tech':user_event_list_nontech}

    return render(request, 'account/selected_events.html', event_dict)
