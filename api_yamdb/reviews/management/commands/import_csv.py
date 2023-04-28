import csv

from django.apps import apps

from django.core.management.base import BaseCommand

# Import csv
TABLE_IMPORT = {
    'static/data/users.csv': {'users': 'User'},
    'static/data/category.csv': {'reviews': 'Category'},
    'static/data/genre.csv': {'reviews': 'Genre'},
    'static/data/titles.csv': {'reviews': 'Title'},
    'static/data/genre_title.csv': {'reviews': 'GenreTitle'},
    'static/data/review.csv': {'reviews': 'Review'},
    'static/data/comments.csv': {'reviews': 'Comment'}
}


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

    def handle(self, *args, **options):
        """Метод импортирующий csv в базу данных"""
        # Добавляем записи в БД
        for link, tab in TABLE_IMPORT.items():
            _name = list(tab.values())[0]
            _app = list(tab.keys())[0]
            _model = apps.get_model(_app, _name)
            if options['delete_existing']:
                _model.objects.all().delete()
                self.stdout.write(self.style.SUCCESS(
                    f'Таблица {_name} очищена от старых записей.'))
            # Подсчет добавляемых строк
            with open(link, 'r') as csvfile:
                count_row = len(list(csv.DictReader(csvfile)))

            with open(link,
                      'r',
                      encoding='utf-8') as csvfile:
                dict_reader = csv.DictReader(csvfile)

                if _name == 'Title':
                    records = []
                    for i in dict_reader:
                        record = _model(
                            id=i['id'],
                            name=i['name'],
                            year=i['year'],
                            category_id=i['category']
                        )
                        records.append(record)
                    _model.objects.bulk_create(records)
                    self.stdout.write(self.style.SUCCESS(
                        f'Добавлено {count_row} записей в таблицу {_name}.'))
                    continue

                if _name == 'Review':
                    records = []
                    for i in dict_reader:
                        record = _model(
                            id=i['id'],
                            title_id=i['title_id'],
                            text=i['text'],
                            author_id=i['author'],
                            score=i['score'],
                            pub_date=i['pub_date']
                        )
                        records.append(record)
                    _model.objects.bulk_create(records)
                    self.stdout.write(self.style.SUCCESS(
                        f'Добавлено {count_row} записей в таблицу {_name}.'))
                    continue

                if _name == 'Comment':
                    records = []
                    for i in dict_reader:
                        record = _model(
                            id=i['id'],
                            review_id=i['review_id'],
                            text=i['text'],
                            author_id=i['author'],
                            pub_date=i['pub_date']
                        )
                        records.append(record)
                    _model.objects.bulk_create(records)
                    self.stdout.write(self.style.SUCCESS(
                        f'Добавлено {count_row} записей в таблицу {_name}.'))
                    continue

                _model.objects.bulk_create(
                    _model(**data) for data in dict_reader
                )
            self.stdout.write(self.style.SUCCESS(
                f'Добавлено {count_row} записей в таблицу {_name}.'))
