# Generated by Django 4.2.1 on 2023-05-06 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produitApp', '0002_alter_produit_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produitinofficine',
            name='fullname',
        ),
        migrations.AlterField(
            model_name='produitinofficine',
            name='quantite',
            field=models.IntegerField(default=0),
        ),
    ]
