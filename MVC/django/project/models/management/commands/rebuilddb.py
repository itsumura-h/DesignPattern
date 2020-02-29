from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = "My shiny new management command."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        subprocess.call(['python', 'manage.py', 'migrate', 'models', 'zero'])
        subprocess.call(['rm', '-fr', 'models/migrations/'])
        subprocess.call(['mkdir', 'models/migrations'])
        subprocess.call(['touch', 'models/migrations/__init__.py'])
        subprocess.call(['python', 'manage.py', 'makemigrations'])
        subprocess.call(['python', 'manage.py', 'migrate'])
