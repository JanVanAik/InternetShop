from django.core.management import BaseCommand

from users.models import User, UserProfile


class Command(BaseCommand):
    def handle(self, *args, **options):
        print('_' * 60)
        exclude_idx = UserProfile.objects.only('user').values_list('user__id', flat=True)
        users = User.objects.exclude(id__in=exclude_idx).only('id').distinct()
        if users.exists():
            create_profiles = [UserProfile(user=user) for user in users]
            UserProfile.objects.bulk_create(create_profiles)
        print('_' * 60)
