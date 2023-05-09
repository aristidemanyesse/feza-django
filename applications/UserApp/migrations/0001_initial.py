# Generated by Django 4.2 on 2023-05-02 22:03

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('officineApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('deleted', models.BooleanField(default=False)),
                ('protected', models.BooleanField(default=False)),
                ('fullname', models.CharField(blank=True, max_length=255, null=True)),
                ('telephone', models.CharField(blank=True, max_length=255, null=True)),
                ('otp', models.CharField(blank=True, max_length=6, null=True)),
                ('contact', models.CharField(blank=True, max_length=255, null=True)),
                ('is_valide', models.BooleanField(default=True)),
                ('image', models.ImageField(blank=True, default='default.png', max_length=255, null=True, upload_to='stockage/images/employes/')),
                ('circonscription', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agence_employe', to='officineApp.circonscription')),
            ],
        ),
    ]