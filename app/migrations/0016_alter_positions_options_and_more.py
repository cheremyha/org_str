# Generated by Django 4.1 on 2022-08-14 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_positions_alter_employees_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='positions',
            options={'verbose_name': 'Должность', 'verbose_name_plural': 'Должности в компании'},
        ),
        migrations.AlterField(
            model_name='positions',
            name='position_name',
            field=models.CharField(max_length=30, verbose_name='Должность'),
        ),
    ]
