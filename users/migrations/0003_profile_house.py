# Generated by Django 5.1 on 2024-09-04 13:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
        ('users', '0002_alter_profile_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='house',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='members', to='house.house'),
        ),
    ]
