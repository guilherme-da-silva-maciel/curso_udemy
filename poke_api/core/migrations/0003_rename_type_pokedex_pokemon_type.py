# Generated by Django 4.0.4 on 2022-04-28 17:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_rename_type_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pokedex',
            old_name='type',
            new_name='pokemon_type',
        ),
    ]