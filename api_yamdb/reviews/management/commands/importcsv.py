import csv
from django.core.management.base import BaseCommand, CommandError



class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('static/data/users.csv', 'r', encoding='utf-8') as csvfile:
            dict_reader = csv.DictReader(csvfile)
            for row in dict_reader:

        for _ in range(size):
            kwargs = {
                'day': self.get_date(),
                'closing_record': random.randint(1, 1000)
            }
            record = StockRecord(**kwargs)
            records.append(record)
        if options["delete_existing"]:
            StockRecord.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Existing stock records deleted.'))
        StockRecord.objects.bulk_create(records)