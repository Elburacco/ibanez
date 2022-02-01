from django.conf import settings
from django.core.management.base import BaseCommand, CommandError

from allauth.socialaccount.models import SocialApp


class Command(BaseCommand):
    help = 'Loads allauth SocialApp settings into database'

    def handle(self, *args, **options):
        for provider, config in settings.SOCIAL_ACCOUNT_APPS.items():
            try:
                social_app = SocialApp(provider=provider,
                                       name=config['SOCIAL_AUTH_NAME'],
                                       client_id=config['SOCIAL_AUTH_ID'],
                                       secret=config['SOCIAL_AUTH__SECRET_KEY'])
                social_app.save()
                social_app.sites.set([settings.SITE_ID])
                social_app.save()

                self.stdout.write(self.style.SUCCESS(
                    'Successfully created app: {}'.format(social_app)))
            except:
                raise CommandError('Error creating social app.')
