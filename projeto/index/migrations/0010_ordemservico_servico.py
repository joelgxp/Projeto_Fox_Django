# Generated by Django 5.0.1 on 2024-03-19 12:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0009_remove_ordemservico_servicos'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordemservico',
            name='servico',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='index.servico'),
            preserve_default=False,
        ),
    ]