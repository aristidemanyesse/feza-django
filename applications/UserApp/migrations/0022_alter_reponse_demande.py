# Generated by Django 4.1 on 2023-07-01 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('UserApp', '0021_alter_reponse_demande'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reponse',
            name='demande',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='demande_reponse', to='UserApp.officinedemande'),
        ),
    ]
