import csv

from django.core.management.base import BaseCommand
from reviews.models import Category, Comment, Genre, GenreTitle, Review, Title
from users.models import User


class Command(BaseCommand):
    help = "Импонтировать данные из csv"

    def add_arguments(self, parser):
        """Использование опционального не обязательного аргумента"""
        parser.add_argument(
            '-d',
            action='store_true',
            dest='delete_existing',
            default=False,
            help='Удалить существующие записи перед созданием новых',
        )

    def handle(self, *args, **options): # noqa
        """Метод импортирующий csv в базу данных"""
        # Добавляем User
        records = []
        with open('static/data/users.csv',
                  'r',
                  encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for row in dict_reader:
                record = User(**row)
                records.append(record)
            count_row = dict_reader.line_num - 1
            name = type(record).__name__

            if options['delete_existing']:
                User.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица {name} очищена от старых записей.'))
            User.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {count_row} записей в таблицу {name}.'))

        # Добавляем Category
        records = []
        with open('static/data/category.csv',
                  'r',
                  encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for row in dict_reader:
                record = Category(**row)
                records.append(record)
            count_row = dict_reader.line_num - 1
            name = type(record).__name__

            if options['delete_existing']:
                Category.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица {name} очищена от старых записей.'))
            Category.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {count_row} записей в таблицу {name}.'))

        # Добавляем Genre
        records = []
        with open('static/data/genre.csv',
                  'r',
                  encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for row in dict_reader:
                record = Genre(**row)
                records.append(record)
            count_row = dict_reader.line_num - 1
            name = type(record).__name__

            if options['delete_existing']:
                Genre.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица {name} очищена от старых записей.'))
            Genre.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {count_row} записей в таблицу {name}.'))

        # Добавляем Title
        records = []
        with open('static/data/titles.csv',
                  'r',
                  encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for i in dict_reader:
                record = Title(
                    id=i['id'],
                    name=i['name'],
                    year=i['year'],
                    category_id=i['category']
                )
                records.append(record)
            count_row = dict_reader.line_num - 1
            name = type(record).__name__

            if options['delete_existing']:
                Title.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица {name} очищена от старых записей.'))
            Title.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {count_row} записей в таблицу {name}.'))

        # Добавляем GenreTitle
        records = []
        with open('static/data/genre_title.csv',
                  'r',
                  encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for i in dict_reader:
                record = GenreTitle(
                    id=i['id'],
                    genre_id=i['genre_id'],
                    title_id=i['title_id']
                )
                records.append(record)
            count_row = dict_reader.line_num - 1
            name = type(record).__name__

            if options['delete_existing']:
                GenreTitle.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица {name} очищена от старых записей.'))
            GenreTitle.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {count_row} записей в таблицу {name}.'))

        # Добавляем Review
        records = []
        with open('static/data/review.csv',
                  'r',
                  encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for i in dict_reader:
                record = Review(
                    id=i['id'],
                    title_id=i['title_id'],
                    text=i['text'],
                    author_id=i['author'],
                    score=i['score'],
                    pub_date=i['pub_date']
                )
                records.append(record)
            count_row = dict_reader.line_num - 1
            name = type(record).__name__

            if options['delete_existing']:
                Review.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица {name} очищена от старых записей.'))
            Review.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {count_row} записей в таблицу {name}.'))

        # Добавляем Comment
        records = []
        with open('static/data/comments.csv',
                  'r',
                  encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for i in dict_reader:
                record = Comment(
                    id=i['id'],
                    review_id=i['review_id'],
                    text=i['text'],
                    author_id=i['author'],
                    pub_date=i['pub_date']
                )
                records.append(record)
            count_row = dict_reader.line_num - 1
            name = type(record).__name__

            if options['delete_existing']:
                Comment.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица {name} очищена от старых записей.'))
            Comment.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {count_row} записей в таблицу {name}.'))
