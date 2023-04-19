import csv
from django.core.management.base import BaseCommand, CommandError
from users.models import User
from reviews.models import Category, Genre, GenreTitle, Title, Review, Comment



class Command(BaseCommand):
    help = "Импонтировать данные из csv"

    def add_arguments(self, parser):
        # Named (optional) arguments
        parser.add_argument(
            '-d',
            action='store_true',
            dest='delete_existing',
            default=False,
            help='Удалить существующие записи перед созданием новых',
        )

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

            if options['delete_existing']:
                User.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица User очищена от старых записей.'))
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

            if options['delete_existing']:
                Category.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица Category очищена от старых записей.'))
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

            if options['delete_existing']:
                Genre.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица Genre очищена от старых записей.'))
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
                    id=i['id'],
                    name=i['name'],
                    year=i['year'],
                    category_id=i['category']
                )
                records.append(record)
                n += 1

            if options['delete_existing']:
                Title.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица Title очищена от старых записей.'))
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
                    id=i['id'],
                    genre_id=i['genre_id'],
                    title_id=i['title_id']
                )
                records.append(record)
                n += 1

            if options['delete_existing']:
                GenreTitle.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица GenreTitle очищена от старых записей.'))
            GenreTitle.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {n} записей в таблицу GenreTitle.'
            ))

        # Добавляем Review
        records = []
        with open('static/data/review.csv',
                  'r',
                  encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            n = 0
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
                n += 1

            if options['delete_existing']:
                Review.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица Review очищена от старых записей.'))
            Review.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {n} записей в таблицу Review.'
            ))

        # Добавляем Comment
        records = []
        with open('static/data/comments.csv',
                  'r',
                  encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            n = 0
            for i in dict_reader:
                record = Comment(
                    id=i['id'],
                    review_id=i['review_id'],
                    text=i['text'],
                    author_id=i['author'],
                    pub_date=i['pub_date']
                )
                records.append(record)
                n += 1

            if options['delete_existing']:
                Comment.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица Comment очищена от старых записей.'))
            Comment.objects.bulk_create(records)
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {n} записей в таблицу Comment.'
            ))
