import subprocess
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'マイグレーション履歴の削除、マイグレーションファイルの再生成、マイグレートするコマンド'

    def handle(self, *args, **options):
        subprocess.call(['python', 'manage.py', 'migrate', 'models', 'zero'])
        subprocess.call(['rm', '-fr', 'models/migrations'])
        subprocess.call(['mkdir', 'models/migrations'])
        subprocess.call(['touch', 'models/migrations/__init__.py'])
        subprocess.call(['python', 'manage.py', 'makemigrations'])
        subprocess.call(['python', 'manage.py', 'migrate'])
        subprocess.call(['python', 'manage.py', 'runseed'])