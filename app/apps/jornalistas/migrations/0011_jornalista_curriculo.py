# Generated by Django 4.2.4 on 2023-12-06 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornalistas', '0010_alter_jornalista_show_associacoes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornalista',
            name='curriculo',
            field=models.FileField(blank=True, null=True, upload_to='curriculos/%Y/%m/%d/'),
        ),
    ]
