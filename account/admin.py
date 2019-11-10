from django.contrib import admin
from .models import Profile, Participation_Tech, Participation_NonTech, Event_Technical, Event_Non_Technical

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','full_name','phone','college','year','payment_status')
    list_filter=('user','college','year','payment_status')

@admin.register(Event_Non_Technical)
class Event_Non_TechnicalAdmin(admin.ModelAdmin):
    list_display=('event_name_non_tech',)
    list_filter=('event_name_non_tech',)

@admin.register(Event_Technical)
class Event_TechnicalAdmin(admin.ModelAdmin):
    list_display=('event_name_tech',)
    list_filter=('event_name_tech',)

@admin.register(Participation_Tech)
class Participation_TechAdmin(admin.ModelAdmin):
    list_display=('participant', 'full_name','event')
    list_filter=('participant', 'event')

@admin.register(Participation_NonTech)
class Participation_NonTechAdmin(admin.ModelAdmin):
    list_display=('participant', 'full_name', 'event')
    list_filter=('participant', 'event')
