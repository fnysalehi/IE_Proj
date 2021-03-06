# Generated by Django 2.1.5 on 2019-01-19 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game_backend', '0005_gamereview'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
                ('loser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='loser', to='game_backend.Profile')),
                ('winner', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='winner', to='game_backend.Profile')),
            ],
        ),
    ]
