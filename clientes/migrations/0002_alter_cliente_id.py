# Generated by Django 3.2.10 on 2024-06-11 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
