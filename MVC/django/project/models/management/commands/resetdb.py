from django.core.management.base import BaseCommand
import subprocess


class Command(BaseCommand):
    help = "My shiny new management command."

    # def add_arguments(self, parser):
    #     parser.add_argument('sample', nargs='+')

    def handle(self, *args, **options):
        subprocess.call(['python', 'manage.py', 'flush'])
        subprocess.call(['python', 'manage.py', 'loadcsv'])
