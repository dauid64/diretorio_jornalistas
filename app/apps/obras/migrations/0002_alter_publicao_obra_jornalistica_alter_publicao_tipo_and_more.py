# Generated by Django 4.2.4 on 2023-12-06 16:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('opcoes', '0001_initial'),
        ('obras', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicao',
            name='obra_jornalistica',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='obras.obrajornalistica'),
        ),
        migrations.AlterField(
            model_name='publicao',
            name='tipo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='opcoes.tipodepublicacao'),
        ),
        migrations.AlterField(
            model_name='publicao',
            name='veiculo_de_comunicacao',
            field=models.CharField(max_length=55),
        ),
    ]
