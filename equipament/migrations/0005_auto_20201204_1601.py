# Generated by Django 3.1.4 on 2020-12-04 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipament', '0004_antenna'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Parameters',
            new_name='Point',
        ),
        migrations.AlterModelOptions(
            name='point',
            options={'verbose_name': 'Punto Medio', 'verbose_name_plural': 'Puntos Medios'},
        ),
    ]