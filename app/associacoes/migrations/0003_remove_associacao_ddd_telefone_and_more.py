# Generated by Django 4.2.4 on 2023-09-19 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('associacoes', '0002_alter_associacao_cnpj'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='associacao',
            name='ddd_telefone',
        ),
        migrations.AlterField(
            model_name='associacao',
            name='telefone',
            field=models.CharField(),
        ),
    ]
