# Generated by Django 4.0 on 2023-11-08 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('opcoes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ObraJornalistica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=254)),
                ('descricao', models.CharField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Publicao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('link', models.URLField(blank=True, max_length=254, null=True)),
                ('anexo', models.ImageField(blank=True, null=True, upload_to=None)),
                ('obra_jornalistica', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='obras.obrajornalistica')),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='opcoes.tipodepublicacao')),
                ('veiculo_de_comunicacao', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='opcoes.veiculodecomunicacao')),
            ],
        ),
        migrations.CreateModel(
            name='Livro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn10', models.IntegerField(blank=True, null=True)),
                ('isbn13', models.IntegerField(blank=True, null=True)),
                ('editora', models.CharField(max_length=254)),
                ('paginas', models.IntegerField()),
                ('cidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='opcoes.cidades')),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='opcoes.estados')),
                ('obra_jornalistica', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='obras.obrajornalistica')),
            ],
        ),
    ]
