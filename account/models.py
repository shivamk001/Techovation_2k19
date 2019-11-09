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
    first_name = models.CharField(max_length=100,null=False,blank=False,default='First')
    last_name = models.CharField(max_length=100,null=False,blank=False,default='Last')
    email = models.EmailField(null=False,blank=False,default='abc@gmail.com')
    phone = models.CharField(max_length=14,null=True,blank=True,unique=False, default='+919999999999')

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
    year=models.CharField(max_length=30,null=False, choices=YEAR_CHOICES,default='first')

    payment_status=models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'

@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
