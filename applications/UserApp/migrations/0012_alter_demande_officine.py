# Generated by Django 4.1 on 2023-06-29 13:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('officineApp', '0016_merge_20230629_1233'),
        ('UserApp', '0011_remove_lignedemande_is_available_lignedemande_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='demande',
            name='officine',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='officine_demande', to='officineApp.officine'),
        ),
    ]
