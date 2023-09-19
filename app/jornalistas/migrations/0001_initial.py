# Generated by Django 4.2.4 on 2023-09-19 03:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('associacoes', '0002_alter_associacao_cnpj'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricoProfissional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=254)),
                ('cargo', models.CharField(max_length=254)),
                ('data_inicio', models.DateField()),
                ('data_de_termino', models.DateField(blank=True, null=True)),
                ('referencia', models.CharField(max_length=254)),
                ('contato_da_referencia', models.CharField(max_length=254)),
                ('validado', models.BooleanField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Jornalista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_de_guerra', models.CharField(max_length=50)),
                ('nome', models.CharField(max_length=255)),
                ('sobrenome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=11)),
                ('data_de_nascimento', models.DateField(blank=True, null=True)),
                ('telefone', models.CharField(blank=True, max_length=50, null=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='')),
                ('registro', models.CharField(blank=True, max_length=50, null=True)),
                ('diploma', models.ImageField(upload_to=None)),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
                ('aprovado', models.BooleanField(default=False)),
                ('associacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='associacoes.associacao')),
            ],
        ),
    ]
