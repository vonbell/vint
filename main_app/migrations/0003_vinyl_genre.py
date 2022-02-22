# Generated by Django 4.0.2 on 2022-02-22 02:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_remove_vinyl_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='vinyl',
            name='genre',
            field=models.CharField(choices=[('PP', 'Pop'), ('RK', 'Rock'), ('HH', 'Hip-Hop'), ('FK', 'Folk'), ('CY', 'Country'), ('RB', 'R&B'), ('JZ', 'Jazz'), ('BL', 'Blues'), ('CL', 'Classical'), ('EL', 'Electronic'), ('DC', 'Dance'), ('KP', 'K-Pop'), ('CN', 'Christian'), ('GO', 'Gospel'), ('CO', 'Comedy'), ('OL', 'Oldies'), ('RG', 'Reggae'), ('AP', 'Afro Pop'), ('SO', 'Soul'), ('AL', 'Alternative'), ('IE', 'Indie'), ('WW', 'Worldwide')], default='PP', max_length=2),
        ),
    ]
