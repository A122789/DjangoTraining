# Generated by Django 3.2.4 on 2021-06-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='error',
            fields=[
                ('errordatetime', models.DateField()),
                ('errorid', models.IntegerField(primary_key=True, serialize=False)),
                ('errordescription', models.CharField(max_length=4000)),
                ('assigneddatetime', models.DateField()),
                ('assignedreason', models.CharField(max_length=8000)),
            ],
            options={
                'db_table': 'Error_Log',
                'managed': False,
            },
        ),
    ]
