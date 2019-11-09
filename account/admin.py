from django.contrib import admin
from .models import Profile
# Register your models here.

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user','full_name','phone','college','year','payment_status')
    list_filter=('user','college','year','payment_status')
