# Generated by Django 4.1 on 2022-09-03 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'places',
            },
        ),
    ]
