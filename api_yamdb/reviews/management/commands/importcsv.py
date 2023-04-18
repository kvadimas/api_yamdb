import csv
from django.core.management.base import BaseCommand, CommandError
from users.models import User
from reviews.models import Category, Genre, GenreTitle, Title



class Command(BaseCommand):
    help = "Import data from csv"

    def handle(self, *args, **options):
        # Добавляем User
        records = []
        with open('static/data/users.csv') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            n = 0
            for row in dict_reader:
                record = User(**row)
                records.append(record)
                n += 1

            User.objects.all().delete()
            User.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {n} записей в таблицу User.'))

        # Добавляем Category
        records = []
        with open('static/data/category.csv',
                  'r',
                  encoding='utf-8'
                ) as csvfile:
            dict_reader = csv.DictReader(csvfile)
            n = 0
            for row in dict_reader:
                record = Category(**row)
                records.append(record)
                n += 1

            Category.objects.all().delete()
            Category.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {n} записей в таблицу Category.'))

        # Добавляем Genre
        records = []
        with open('static/data/genre.csv',
                  'r',
                  encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            n = 0
            for row in dict_reader:
                record = Genre(**row)
                records.append(record)
                n += 1

            Genre.objects.all().delete()
            Genre.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {n} записей в таблицу Genre.'
            ))

        # Добавляем Title
        records = []
        with open('static/data/titles.csv',
                  'r',
                  encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            n = 0
            for i in dict_reader:
                record = Title(
                    i['id'],
                    i['name'],
                    i['year'],
                    i['category']
                )
                records.append(record)
                n += 1

            Title.objects.all().delete()
            Title.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {n} записей в таблицу Title.'
            ))

        # Добавляем GenreTitle
        records = []
        with open('static/data/genre_title.csv',
                  'r',
                  encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            n = 0
            for i in dict_reader:
                record = GenreTitle(
                    i['id'],
                    i['genre_id'],
                    i['title_id']
                )
                records.append(record)
                n += 1

            GenreTitle.objects.all().delete()
            GenreTitle.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {n} записей в таблицу GenreTitle.'
            ))
