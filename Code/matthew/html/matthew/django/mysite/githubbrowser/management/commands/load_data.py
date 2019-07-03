

from django.core.management.base import BaseCommand
import requests
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        response = requests.get('https://api.github.com/search/repositories?q=hello+world')
        data = json.loads(response.text)
        print(data)
