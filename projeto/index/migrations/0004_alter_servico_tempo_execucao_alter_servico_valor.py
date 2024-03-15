# Generated by Django 5.0.1 on 2024-03-15 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_servico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='tempo_execucao',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='servico',
            name='valor',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
    ]
