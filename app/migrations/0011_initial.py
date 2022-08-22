# Generated by Django 4.1 on 2022-08-14 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0010_delete_employees'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, unique=True)),
                ('depth', models.PositiveIntegerField()),
                ('numchild', models.PositiveIntegerField(default=0)),
                ('firs_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('position', models.CharField(max_length=30)),
                ('date_employment', models.DateField()),
                ('salary', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
