import csv

from django.core.management.base import BaseCommand
from django.db import IntegrityError

from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones data from CSV file'

    def handle(self, *args, **options):
        with open('phones.csv') as csvfile:
            phone_reader = csv.reader(csvfile, delimiter=';')
            next(phone_reader)

            for line in phone_reader:
                phone = Phone(
                    name=line[1],
                    price=line[3],
                    image=line[2],
                    release_date=line[4],
                    lte_exists=line[5]
                )
                try:
                    phone.save()
                except IntegrityError:
                    pass
