# Generated by Django 4.1 on 2023-06-29 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produitApp', '0011_alter_typeproduit_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
