# Generated by Django 5.0.1 on 2024-03-21 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0011_remove_servico_id_veiculo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordemservico',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
