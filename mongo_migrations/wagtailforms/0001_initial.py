# Generated by Django 5.0.10.dev20241112012728 on 2024-12-03 20:22

import django.core.serializers.json
import django.db.models.deletion
import django_mongodb_backend.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormSubmission',
            fields=[
                ('id', django_mongodb_backend.fields.ObjectIdAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_data', models.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('submit_time', models.DateTimeField(auto_now_add=True, verbose_name='submit time')),
                ('page', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.page')),
            ],
            options={
                'verbose_name': 'form submission',
                'verbose_name_plural': 'form submissions',
                'abstract': False,
            },
        ),
    ]
