# Generated by Django 5.0.10.dev20241112012728 on 2024-12-03 20:35

import django.db.models.deletion
import django_mongodb.fields
import wagtail.users.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', django_mongodb.fields.ObjectIdAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submitted_notifications', models.BooleanField(default=True, help_text='Receive notification when a page is submitted for moderation', verbose_name='submitted notifications')),
                ('approved_notifications', models.BooleanField(default=True, help_text='Receive notification when your page edit is approved', verbose_name='approved notifications')),
                ('rejected_notifications', models.BooleanField(default=True, help_text='Receive notification when your page edit is rejected', verbose_name='rejected notifications')),
                ('updated_comments_notifications', models.BooleanField(default=True, help_text='Receive notification when comments have been created, resolved, or deleted on a page that you have subscribed to receive comment notifications on', verbose_name='updated comments notifications')),
                ('preferred_language', models.CharField(default='', help_text='Select language for the admin', max_length=10, verbose_name='preferred language')),
                ('current_time_zone', models.CharField(default='', help_text='Select your current time zone', max_length=40, verbose_name='current time zone')),
                ('avatar', models.ImageField(blank=True, upload_to=wagtail.users.models.upload_avatar_to, verbose_name='profile picture')),
                ('dismissibles', models.JSONField(blank=True, default=dict)),
                ('theme', models.CharField(choices=[('system', 'System default'), ('light', 'Light'), ('dark', 'Dark')], default='system', max_length=40, verbose_name='admin theme')),
                ('contrast', models.CharField(choices=[('system', 'System default'), ('more_contrast', 'More contrast')], default='system', max_length=40, verbose_name='contrast')),
                ('density', models.CharField(choices=[('default', 'Default'), ('snug', 'Snug')], default='default', max_length=40, verbose_name='density')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='wagtail_userprofile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user profile',
                'verbose_name_plural': 'user profiles',
            },
        ),
    ]