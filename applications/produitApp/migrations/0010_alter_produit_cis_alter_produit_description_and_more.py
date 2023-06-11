# Generated by Django 4.2.1 on 2023-06-11 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produitApp', '0009_produit_cis_produit_forme_produit_voies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='cis',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='forme',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='produit',
            name='voies',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
