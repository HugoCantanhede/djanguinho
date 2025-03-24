# Generated by Django 5.1.7 on 2025-03-24 19:29

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuário',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('sobrenome', models.CharField(max_length=50)),
                ('cpf', models.CharField(max_length=11)),
                ('telefone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('endereco', models.CharField(max_length=100)),
                ('data_cadastro', models.DateTimeField(default=django.utils.timezone.now)),
                ('ativo', models.BooleanField(default=True)),
            ],
        ),
    ]
