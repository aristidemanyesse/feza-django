# Generated by Django 4.2.1 on 2023-05-06 01:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produitApp', '0003_remove_produitinofficine_fullname_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stockstate',
            name='etiquette',
        ),
        migrations.RemoveField(
            model_name='stockstate',
            name='name',
        ),
    ]