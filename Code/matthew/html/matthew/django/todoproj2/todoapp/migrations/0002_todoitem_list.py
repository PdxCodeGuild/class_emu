# Generated by Django 2.1.5 on 2019-04-18 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='todoapp.TodoList'),
            preserve_default=False,
        ),
    ]
