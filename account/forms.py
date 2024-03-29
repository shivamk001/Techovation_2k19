from django import forms
from django.contrib.auth.models import User
from .models import Profile, Participation_Tech, Participation_NonTech, Event_Technical, Event_Non_Technical
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)#, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=True)#, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    #phone_num = PhoneNumberField(null=False,blank=False,unique=False, default='+919999999999')
    phone_number = forms.CharField(min_length=10, max_length=10, required=True, help_text='Please enter your correct phone number')
    college = forms.CharField(max_length=100, required=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password1', 'password2')

'''
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
'''

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

## THIS ALLOWS USERS TO EDIT THIer first name, last name, and email
## WHICH ARE ATTRIBUTES OF THE BUILT_IN DJANGO Model

class UserEditForm(forms.ModelForm):
    '''
    first_name = forms.CharField(max_length=30, required=False, strip=True)#empty_value=True,
    last_name = forms.CharField(max_length=30, required=False,strip=True)#empty_value=True, strip=True)
    #email = forms.CharField(max_length=30, required=False,empty_value=True, strip=True)

    college = forms.CharField(max_length=100, required=False,strip=True)#empty_value=True, strip=True)

    YEAR_CHOICES=(
    ('First Year','First Year'),
    ('Second Year','Second Year'),
    ('Third Year','Third Year'),
    ('Forth Year','Forth Year'),
    ('Diploma First Year','Diploma First Year'),
    ('Diploma Second Year','Diploma Second Year'),
    ('Diploma Third Year','Diploma Third Year'),
    )
    year = forms.CharField(max_length=30, choices=YEAR_CHOICES,default='first')
    '''
    first_name = forms.CharField(max_length=30, required=False, strip=True)#empty_value=True,
    last_name = forms.CharField(max_length=30, required=False,strip=True)#empty_value=True, strip=True)
    phone_number = forms.CharField(min_length=10, max_length=10, required=False,strip=True)#empty_value=True, strip=True)
    college_name = forms.CharField(max_length=100, required=False,strip=True)#empty_value=True, strip=True)
    class Meta:
        model = Profile
        fields= ('first_name', 'last_name', 'phone_number', 'college_name', 'year')

class AddEventsTech(forms.ModelForm):
    class Meta:
        model = Event_Technical
        fields = ('event_name_tech',)

class AddEventsNonTech(forms.ModelForm):
    class Meta:
        model = Event_Non_Technical
        fields = ('event_name_non_tech',)
