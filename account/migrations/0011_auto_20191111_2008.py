# Generated by Django 2.2.7 on 2019-11-11 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20191111_1954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_non_technical',
            name='event_name_non_tech',
            field=models.CharField(choices=[('KAVYANIKAL', 'KAVYANIKAL'), ('SOLICIT', 'SOLICIT'), ('HINDI DEBATE', 'HINDI DEBATE'), ('ENGLISH DEBATE', 'ENGLISH DEBATE'), ('PPT', 'PPT'), ('SELFIVATION', 'SELFIVATION'), ('CAPTURE THE MOMENT', 'CAPTURE THE MOMENT'), ('DANGORIUS', 'DANGORIUS'), ('MIX CRICKET', 'MIX CRICKET'), ('FUTSAL', 'FUTSAL'), ('ARM WRESTLING', 'ARM WRESTLING'), ('BLIND HURDLE', 'BLIND HURDLE'), ('TUG OF WAR', 'TUG OF WAR'), ('MUSICAL CHAIR', 'MUSICAL CHAIR'), ('SKETHCHING', 'SKETHCHING'), ('WALL PAINTING', 'WALL PAINTING'), ('STREET PAINTING', 'STREET PAINTING'), ('RANGOLI', 'RANGOLI'), ('TREASURE HUNT', 'TREASURE HUNT'), ('AD-MAD', 'AD-MAD'), ('SNAKE & LADDER', 'SNAKE & LADDER'), ('PUBG', 'PUBG'), ('NEED FOR SPEED', 'NEED FOR SPEED'), ('TEKKEN', 'TEKKEN'), ('DRAG RACE', 'DRAG RACE'), ('DART', 'DART'), ('KNOW YOUR PARTNER', 'KNOW YOUR PARTNER'), ('THE RUBIKS CUBE', 'THE RUBIKS CUBE')], help_text='Enter Event Name (e.g. Futsal)', max_length=200),
        ),
    ]
