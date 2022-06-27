# Generated by Django 4.0.5 on 2022-06-27 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ComputerModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('ram', models.IntegerField()),
                ('diagonal', models.IntegerField()),
            ],
            options={
                'db_table': 'computers',
            },
        ),
    ]
