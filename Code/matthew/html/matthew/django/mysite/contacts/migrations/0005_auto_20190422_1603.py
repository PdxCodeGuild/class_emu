# Generated by Django 2.1.5 on 2019-04-22 23:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20190422_1530'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='eye_color',
            new_name='eye_colors',
        ),
    ]
