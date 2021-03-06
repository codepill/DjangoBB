from optparse import make_option
from datetime import datetime

from django.core.management.base import BaseCommand, CommandError
from djangobb_forum.models import Ban


class Command(BaseCommand):

    option_list = BaseCommand.option_list + (
        make_option('--all', action='store_true', dest='all', default=False, 
                    help=u'Unban all users'),
        make_option('--by-time', action='store_true', dest='by-time', default=False, 
                    help=u'Unban users by time'),
    )
    help = u'Unban users'

    def handle(self, *args, **options):
        if options['all']:
            Ban.objects.all().delete()
        elif options['by-time']:
            Ban.objects.filter(ban_end__lte=datetime.now()).delete()
        else:
            raise CommandError('Invalid options')
