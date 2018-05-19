from django.core.management.base import BaseCommand

from friends.tasks import friends_check

class Command(BaseCommand):

    help = 'Random friends behavior'

    def handle(self, *args, **options):
        friends_check()
