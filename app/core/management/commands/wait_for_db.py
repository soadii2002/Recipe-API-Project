'''
    django management command to wait for the database to be available.
    This is useful in containerized environments where the database may not be ready when the application starts
'''
import time

from psycopg2 import OperationalError as Psycopg2Error

from django.db.utils import OperationalError

from django.core.management.base import BaseCommand

class Command (BaseCommand):
    ''' django command to wait for the database '''
    def handle(self, *args, **options):
        "entrypoint for the command"
        self.stdout.write("Waiting for database...")
        db_up = False
        while db_up is False:
            try:
                self.check(databases=["default"])
                db_up = True  
            except(Psycopg2Error,OperationalError):
                self.stdout.write("Database unavailable, waiting 1 scond...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database is available!"))
