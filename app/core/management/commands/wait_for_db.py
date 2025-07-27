'''
    django management command to wait for the database to be available.
    This is useful in containerized environments where the database may not be ready when the application starts
'''

from django.core.management.base import BaseCommand

class Command (BaseCommand):
    ''' django command to wait for the database '''
    def handle(self, *args, **options):
        pass