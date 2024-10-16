# Generated by Django 5.1.1 on 2024-10-16 10:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TenantModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")),
                ('status', models.BooleanField(default=True, verbose_name='Status ')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Locataire',
                'verbose_name_plural': 'Locataires',
            },
        ),
    ]
