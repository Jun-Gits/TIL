# Generated by Django 2.2.2 on 2019-07-03 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_to_do_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='isDone',
            field=models.BooleanField(default=False),
        ),
    ]
