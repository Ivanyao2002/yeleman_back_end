# Generated by Django 5.1.1 on 2024-10-13 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otptokenmodel',
            name='otp_code',
            field=models.CharField(default='390cd7', max_length=6),
        ),
    ]
