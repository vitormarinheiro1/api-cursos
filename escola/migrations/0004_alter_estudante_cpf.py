# Generated by Django 5.2.4 on 2025-07-04 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escola', '0003_remove_matricula_nivel_matricula_periodo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudante',
            name='cpf',
            field=models.CharField(max_length=11, unique=True),
        ),
    ]
