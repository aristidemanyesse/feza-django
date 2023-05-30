# Generated by Django 4.2.1 on 2023-05-28 08:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('officineApp', '0014_alter_circonscription_options_alter_officine_options'),
        ('UserApp', '0008_alter_utilisateur_imei'),
    ]

    operations = [
        migrations.AlterField(
            model_name='utilisateur',
            name='circonscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='circonscription_utilisateur', to='officineApp.circonscription'),
        ),
    ]