import subprocess
from django.core.management.base import BaseCommand
from models.orator import (
    Auth,
    User
)


class Command(BaseCommand):
    help = 'マイグレーション履歴の削除、マイグレーションファイルの再生成、マイグレートするコマンド'

    def handle(self, *args, **options):
        Auth.insert([{'name': 'admin'}, {'name': 'user'}])

        User.insert([
            {
                'name': f'user{i}',
                'auth_id': 2 if i % 2 == 0 else 1
            }
            for i in range(1, 11)
        ])
