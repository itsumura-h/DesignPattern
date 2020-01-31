from django.core.management.base import BaseCommand
import glob
from app.orator import config
from orator import DatabaseManager
import csv
from tqdm import tqdm
from datetime import datetime

from django.db import connection, transaction
from django.conf import settings


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        db = DatabaseManager(config)
        # CSVファイル一覧の絶対パスを取得
        csv_list = glob.glob("/home/www/models/csv/*.csv")

        # トランザクション開始
        # print("Running seeder")
        with db.transaction():
            for file_path in tqdm(csv_list):
                table_name = file_path.split('/')[-1].split('.')[1]

                with open(file_path, encoding="utf-8") as f:
                    content = [csv_row for csv_row in csv.reader(f)]
                    header = content[0]
                    del content[0]
                    data = content

                    # ヘッダーとデータをマッピングして連想配列に
                    insert_data = []
                    for data_row in data:
                        new_row = {}
                        for i, value in enumerate(data_row):
                            if value == '':
                                value = datetime.now()
                            elif value == 'NULL':
                                value = None
                            elif value == 'TRUE':
                                value = True
                            elif value == 'FALSE':
                                value = False

                            new_row[header[i]] = value

                        insert_data += [new_row]

                    db.table(table_name).insert(insert_data)

        with db.transaction():
            for file_path in tqdm(csv_list):
                table_name = file_path.split('/')[-1].split('.')[1]
                sql = f"SELECT setval('{table_name}_id_seq', (SELECT MAX(id) FROM {table_name}));"

                with connection.cursor() as cursor:
                    # print(sql)
                    cursor.execute(sql)
                    # print(cursor.fetchone())
