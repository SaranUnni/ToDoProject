# Generated by Django 3.2.4 on 2021-06-14 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='date',
            field=models.DateField(default='1998-9-23'),
            preserve_default=False,
        ),
    ]
