# Generated by Django 4.2.8 on 2024-07-30 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornalistas', '0015_jornalista_cidade_jornalista_estado'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornalista',
            name='show_cidade',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name='jornalista',
            name='show_estado',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]