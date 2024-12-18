# Generated by Django 4.2.8 on 2024-07-30 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opcoes', '0002_remove_veiculodecomunicacao_tipo_de_veiculo_and_more'),
        ('jornalistas', '0014_jornalista_show_funcao'),
    ]

    operations = [
        migrations.AddField(
            model_name='jornalista',
            name='cidade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opcoes.cidades'),
        ),
        migrations.AddField(
            model_name='jornalista',
            name='estado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='opcoes.estados'),
        ),
    ]
