# Generated by Django 2.1.5 on 2019-08-05 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='dated_completed',
            new_name='date_completed',
        ),
    ]
