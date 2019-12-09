# Generated by Django 2.1.5 on 2019-08-05 18:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0003_todoitem_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_items', to=settings.AUTH_USER_MODEL),
        ),
    ]