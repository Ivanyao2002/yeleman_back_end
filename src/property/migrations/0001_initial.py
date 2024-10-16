# Generated by Django 5.1.1 on 2024-10-16 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owner', '0001_initial'),
        ('tenant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")),
                ('status', models.BooleanField(default=True, verbose_name='Status ')),
                ('label', models.CharField(max_length=50, verbose_name='Libellé ')),
                ('price', models.IntegerField(verbose_name='Prix ')),
                ('address', models.CharField(max_length=50, verbose_name='Localisation ')),
                ('surface', models.FloatField(verbose_name='Surface ')),
                ('property_type', models.CharField(max_length=100, verbose_name='Type de propriété ')),
                ('description', models.TextField(verbose_name='Description ')),
                ('bedrooms_number', models.IntegerField(verbose_name='Nombre de chambres ')),
                ('video_url', models.URLField(blank=True, null=True, verbose_name='Lien de la vidéo ')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='properties', to='owner.ownermodel')),
            ],
            options={
                'verbose_name': 'Propriété',
                'verbose_name_plural': 'Propriétés',
            },
        ),
        migrations.CreateModel(
            name='DemandModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")),
                ('status', models.BooleanField(default=True, verbose_name='Status ')),
                ('visit_date', models.DateField(blank=True, null=True, verbose_name='Date de visite ')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Commentaire ')),
                ('demand_type', models.CharField(choices=[('LOCATION', 'LOCATION'), ('VISITE', 'VISITE')], default='VISITE', max_length=15, verbose_name='Type de demande ')),
                ('demand_status', models.BooleanField(default=False, verbose_name='Status de la demande ')),
                ('tenant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenant.tenantmodel')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='visits', to='property.propertymodel')),
            ],
            options={
                'verbose_name': 'Demande',
                'verbose_name_plural': 'Demandes',
            },
        ),
        migrations.CreateModel(
            name='CommentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")),
                ('status', models.BooleanField(default=True, verbose_name='Status ')),
                ('content', models.TextField(verbose_name='Commentaire ')),
                ('note', models.IntegerField(verbose_name='Note ')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='property.propertymodel')),
            ],
            options={
                'verbose_name': 'Commentaire',
                'verbose_name_plural': 'Commentaires',
            },
        ),
        migrations.CreateModel(
            name='CharacteristicPropertyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date de création ')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name="Date d'édition ")),
                ('status', models.BooleanField(default=True, verbose_name='Status ')),
                ('swimming_pool', models.BooleanField(verbose_name='Commentaire ')),
                ('green_space', models.BooleanField(verbose_name='Espace vert ')),
                ('air_conditioning', models.BooleanField(verbose_name='Climatisation ')),
                ('nearby_school_or_university', models.BooleanField(verbose_name='A proximité Ecole/Université ')),
                ('commercial_area', models.BooleanField(verbose_name='En zone commerciale ')),
                ('garden', models.BooleanField(verbose_name='Jardin ')),
                ('quiet_area', models.BooleanField(verbose_name='Quartier calme ')),
                ('balcony_terrace', models.BooleanField(verbose_name='Balcon / Terrasse ')),
                ('gym_room', models.BooleanField(verbose_name='Salle de sport ')),
                ('furnished', models.BooleanField(verbose_name='Meublé ')),
                ('furnished_kitchen', models.BooleanField(verbose_name='Cuisine Meublée ')),
                ('city_center', models.BooleanField(verbose_name='En centre-ville ')),
                ('general_condition_new', models.BooleanField(verbose_name='Etat général: Neuf ')),
                ('guardian', models.BooleanField(verbose_name='Gardien ')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='characteristics', to='property.propertymodel')),
            ],
            options={
                'verbose_name': 'Caractéristique',
                'verbose_name_plural': 'Caractéristiques',
            },
        ),
    ]
