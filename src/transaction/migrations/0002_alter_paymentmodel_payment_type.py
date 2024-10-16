# Generated by Django 5.1.1 on 2024-10-16 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymentmodel',
            name='payment_type',
            field=models.CharField(choices=[('Abonnement', 'Abonnement'), ('Paiement de loyer', 'Paiement de loyer')], default='Abonnement', max_length=20, verbose_name='Type de paiement '),
        ),
    ]
