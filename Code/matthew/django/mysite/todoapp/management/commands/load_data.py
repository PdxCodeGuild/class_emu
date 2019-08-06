

from django.core.management.base import BaseCommand


# https://2.python-requests.org/en/master/
import requests

import json

from todoapp.models import TodoItem
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        
        # TodoItem.objects.all().delete()
        
        
        response = requests.get('https://favqs.com/api/qotd')
        data = json.loads(response.text)
        author = data['quote']['author']
        body = data['quote']['body']
        print(f'"{body}" - {author}')
        
        todo_item = TodoItem(text=f'"{body}" - {author}', user=User.objects.get(id=1))
        todo_item.save()
        