# Generated by Django 2.2.7 on 2019-11-09 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(default='+919999999999', max_length=128, region=None, unique=True)),
                ('college', models.CharField(default='IERT', max_length=100)),
                ('year', models.CharField(choices=[('First Year', 'First Year'), ('Second Year', 'Second Year'), ('Third Year', 'Third Year'), ('Forth Year', 'Forth Year'), ('Diploma First Year', 'Diploma First Year'), ('Diploma Second Year', 'Diploma Second Year'), ('Diploma Third Year', 'Diploma Third Year')], default='first', max_length=30)),
                ('payment_status', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
