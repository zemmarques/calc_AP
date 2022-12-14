# Generated by Django 3.2.15 on 2022-08-12 19:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnoLetivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Insira um ano letivo com o formato "aaaa/aaaa". Exemplo: 2020/2021', max_length=12, validators=[django.core.validators.RegexValidator(message='Formato "aaaa/aaaa". Exemplo: 2020/2021', regex='^\\d{4}\\/\\d{4}$')], verbose_name='Designação')),
                ('slug', models.SlugField(blank=True, help_text='Deixar em branco para criar um slug automático e único.', max_length=20, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Ano Letivo',
                'verbose_name_plural': 'Anos Letivos',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Feriado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Designação')),
                ('data', models.DateField(verbose_name='Data')),
                ('concelho', models.CharField(blank=True, max_length=100, null=True, verbose_name='Concelho')),
                ('distrito', models.CharField(blank=True, max_length=100, null=True, verbose_name='Distrito')),
                ('movel', models.BooleanField(default=True, verbose_name='Data móvel')),
                ('tipo', models.CharField(choices=[('nacional', 'Nacional'), ('municipal', 'Municipal')], default='nacional', max_length=100, verbose_name='Tipo')),
                ('slug', models.SlugField(blank=True, help_text='Deixar em branco para criar um slug automático e único.', max_length=20, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('ano_letivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aulas_previstas.anoletivo', verbose_name='Ano Letivo')),
            ],
            options={
                'verbose_name': 'Feriado',
                'verbose_name_plural': 'Feriados',
                'ordering': ['data'],
            },
        ),
        migrations.CreateModel(
            name='Periodo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='Designação')),
                ('tipo', models.CharField(choices=[('1p', '1º Período'), ('2p', '2º Período'), ('3p', '3º Período'), ('natal', 'Natal'), ('carnaval', 'Carnaval'), ('pascoa', 'Páscoa'), ('outro', 'Outro')], max_length=100, verbose_name='Tipo')),
                ('periodo_letivo', models.BooleanField(default=True, verbose_name='Período letivo')),
                ('slug', models.SlugField(blank=True, help_text='Deixar em branco para criar um slug automático e único.', max_length=20, unique=True)),
                ('start_date1', models.DateField(help_text='Usada no 1ºP para definir a data inicial do arranque do ano letivo', verbose_name='Início 1')),
                ('start_date2', models.DateField(blank=True, help_text='Usada no 1ºP para definir a data limite do arranque do ano letivo', null=True, verbose_name='Início 2')),
                ('end_date1', models.DateField(help_text='Usada no 3ºP para os 9º, 11ª e 12º Anos', verbose_name='Fim 1')),
                ('end_date2', models.DateField(blank=True, help_text='Usada no 3ºP para os 5º, 6º, 7º, 8º e 10º Anos', null=True, verbose_name='Fim 2')),
                ('end_date3', models.DateField(blank=True, help_text='Usada no 3ºP para o Pré-escolar e 1º ciclo', null=True, verbose_name='Fim 3')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('ano_letivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aulas_previstas.anoletivo', verbose_name='Ano Letivo')),
            ],
            options={
                'verbose_name': 'Período',
                'verbose_name_plural': 'Períodos',
                'ordering': ['created'],
                'unique_together': {('ano_letivo', 'tipo')},
            },
        ),
    ]
