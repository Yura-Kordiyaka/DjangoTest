# Generated by Django 5.1.1 on 2024-10-02 18:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0002_team_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='owner',
        ),
    ]
