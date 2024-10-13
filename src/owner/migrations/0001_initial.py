# Generated by Django 5.1.1 on 2024-10-13 11:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OwnerModel',
            fields=[
                ('customusermodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('folder_status', models.BooleanField(default=False, verbose_name='Etat du dossier ')),
            ],
            options={
                'verbose_name': 'Propriétaire',
                'verbose_name_plural': 'Propriétaires',
            },
            bases=('base.customusermodel',),
        ),
        migrations.CreateModel(
            name='FolderModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")),
                ('status', models.BooleanField(default=True, verbose_name='Status ')),
                ('acd_number', models.CharField(max_length=30, verbose_name="Numéro de l'ACD ")),
                ('property_type', models.CharField(max_length=30, verbose_name='Type de propriété ')),
                ('localization', models.CharField(max_length=30, verbose_name='Localisation ')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='folders', to='owner.ownermodel')),
            ],
            options={
                'verbose_name': 'Dossier',
                'verbose_name_plural': 'Dossiers',
            },
        ),
    ]
