# Generated by Django 4.2.1 on 2023-05-06 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0003_utilisateur_geometry_alter_utilisateur_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='is_valide',
            field=models.BooleanField(default=False),
        ),
    ]
