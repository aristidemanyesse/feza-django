# Generated by Django 4.1 on 2023-06-29 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0016_reponse_lignereponse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reponse',
            name='demande',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demande_reponse', to='UserApp.demande'),
        ),
    ]
