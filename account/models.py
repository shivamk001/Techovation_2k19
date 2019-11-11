from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField
from django.shortcuts import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100,null=False,blank=False,default='First')
    l_name = models.CharField(max_length=100,null=False,blank=False,default='Last')
    email = models.EmailField(null=False,blank=False,default='abc@gmail.com')
    phone = models.CharField(max_length=10,null=True,blank=True,unique=False, default='9999999999')

    college = models.CharField(max_length=100,null=False,blank=False, default='IERT')

    YEAR_CHOICES=(
    ('First Year','First Year'),
    ('Second Year','Second Year'),
    ('Third Year','Third Year'),
    ('Forth Year','Forth Year'),
    ('Diploma First Year','Diploma First Year'),
    ('Diploma Second Year','Diploma Second Year'),
    ('Diploma Third Year','Diploma Third Year'),
    )
    year = models.CharField(max_length=30,null=False, choices=YEAR_CHOICES,default='first')

    payment_status=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

class Event_Technical(models.Model):
        EVENT_CHOICES = (
        ('AUTO QUIZ','AUTO QUIZ'),
        ('BRIDGE IT','BRIDGE IT'),
        ('BUG-D-CODE','BUG-D-CODE'),
        ('C-LEGACY','C-LEGACY'),
        ('CANVAS','CANVAS'),
        ('CIRCUITEX','CIRCUITEX'),
        ('CODE GOLF','CODE GOLF'),
        ('CODERVATION','CODERVATION'),
        ('DAVIT','DAVIT'),
        ('E-QUIZ','E-QUIZ'),
        ('FAST BOOT','FAST BOOT'),
        ('HURDLE MANIA','HURDLE MANIA'),
        ('IDENTOKIT','IDENTOKIT'),
        ('MODULA','MODULA'),
        ('PATHIK','PATHIK'),
        ('ROBO SOCCER','ROBO SOCCER'),
        ('ROBO WAR','ROBO WAR'),
        ('ROCKET PROPULSION','ROCKET PROPULSION'),
        ('SMART IDEA','SMART IDEA'),
        ('TECH QUIZ','TECH QUIZ'),
        ('TYPE RACER','TYPE RACER'),
        ('UNCHAINED REACTION','UNCHAINED REACTION'),
        ('WEB DEXTRO','WEB-DEXTRO'),
        )

        event_name_tech = models.CharField(max_length=200,choices=EVENT_CHOICES, help_text='Enter Event Name (e.g. CodeGolf)')

        def __str__(self):
            return ("{}".format(self.event_name_tech))

class Event_Non_Technical(models.Model):
    EVENT_CHOICES = (
    ('KAVYANIKAL','KAVYANIKAL'),
    ('SOLICIT', 'SOLICIT'),
    ('HINDI DEBATE','HINDI DEBATE'),
    ('ENGLISH DEBATE','ENGLISH DEBATE'),
    ('PPT','PPT'),
    ('SELFIVATION','SELFIVATION'),
    ('CAPTURE THE MOMENT','CAPTURE THE MOMENT'),
    ('DANGORIUS','DANGORIUS'),
    ('MIX CRICKET','MIX CRICKET'),
    ('FUTSAL','FUTSAL'),
    ('ARM WRESTLING','ARM WRESTLING'),
    ('BLIND HURDLE','BLIND HURDLE'),
    ('TUG OF WAR','TUG OF WAR'),
    ('MUSICAL CHAIR','MUSICAL CHAIR'),
    ('SKETHCHING','SKETHCHING'),
    ('WALL PAINTING','WALL PAINTING'),
    ('STREET PAINTING','STREET PAINTING'),
    ('RANGOLI','RANGOLI'),
    ('TREASURE HUNT','TREASURE HUNT'),
    ('AD-MAD','AD-MAD'),
    ('SNAKE & LADDER','SNAKE & LADDER'),
    ('PUBG','PUBG'),
    ('NEED FOR SPEED','NEED FOR SPEED'),
    ('TEKKEN','TEKKEN'),
    ('DRAG RACE','DRAG RACE'),
    ('DART','DART'),
    ('KNOW YOUR PARTNER','KNOW YOUR PARTNER'),
    ('THE RUBIKS CUBE','THE RUBIKS CUBE'),
    )

    event_name_non_tech = models.CharField(max_length=200,choices=EVENT_CHOICES, help_text='Enter Event Name (e.g. CodeGolf)')

    def __str__(self):
        return ("{}".format(self.event_name_non_tech))

class Participation_Tech(models.Model):
    participant = models.ForeignKey('Profile', on_delete = models.SET_NULL, null =True)
    event = models.ForeignKey('Event_Technical', on_delete = models.CASCADE)

    def __str__(self):
        return f'{self.participant.user.first_name} {self.participant.user.last_name}'

    def full_name(self):
        return f'{self.participant.user.first_name} {self.participant.user.last_name}'

    '''
    def username(self):
        return f'{self.participant.user}'
    '''
    class meta:
        ordering = ['participant', 'event']

class Participation_NonTech(models.Model):
    participant = models.ForeignKey('Profile', on_delete = models.SET_NULL, null =True)
    event = models.ForeignKey('Event_Non_Technical', on_delete = models.CASCADE)

    '''
    def __str__(self):
        return f'{self.participant.user.first_name} {self.participant.user.last_name}'
    '''
    def full_name(self):
        return f'{self.participant.user.first_name} {self.participant.user.last_name}'
    '''
    def username(self):
        return f'{self.participant.user}'
    '''

    class meta:
        ordering = ['participant', 'event']
