# Generated by Django 4.2.1 on 2023-05-10 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0006_alter_utilisateur_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='utilisateur',
            name='imei',
            field=models.CharField(default='', max_length=255, unique=True),
            preserve_default=False,
        ),
    ]
