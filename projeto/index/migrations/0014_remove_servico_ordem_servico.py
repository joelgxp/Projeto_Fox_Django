# Generated by Django 5.0.1 on 2024-03-21 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0013_remove_ordemservico_servico_servico_ordem_servico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servico',
            name='ordem_servico',
        ),
    ]
