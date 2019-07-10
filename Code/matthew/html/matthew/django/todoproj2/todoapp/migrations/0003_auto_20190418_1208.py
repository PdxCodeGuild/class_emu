# Generated by Django 2.1.5 on 2019-04-18 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todoitem_list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='todoapp.TodoList'),
        ),
    ]
