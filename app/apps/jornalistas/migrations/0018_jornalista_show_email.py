# Generated by Django 4.2.8 on 2024-08-26 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornalistas', '0017_jornalista_minibio'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornalista',
            name='show_email',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
