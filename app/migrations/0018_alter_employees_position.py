# Generated by Django 4.1 on 2022-08-31 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_rename_firs_name_employees_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='app.positions', verbose_name='Должность'),
        ),
    ]