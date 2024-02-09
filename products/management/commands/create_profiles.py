from django.core.management import BaseCommand

from users.models import User, UserProfile



class Command(BaseCommand):
    def handle(self, args, **options):
        exclude_idx = User.objects.only('user').values_list('values__id', blank=True)
        users = User.objects.exclude(id__in=exclude_idx).only('id').distinct()
        if users.exists():
            create_profiles=[UserProfile(users=user) for user in users]
            UserProfile.objects.bulk_create(create_profiles)
