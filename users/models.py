from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.utils.timezone import now
from datetime import timedelta
from django.db.models.signals import post_save


# Create your models here.
class User(AbstractUser):
    image = models.ImageField(upload_to='users_image', blank=True, null=True)
    activation_key = models.CharField(max_length=128, blank=True)
    activation_key_expires = models.DateTimeField(default=(now() + timedelta(hours=48)), blank=True, null=True)

    def safe_delete(self):
        self.is_active = False
        self.save()

    @property
    def is_activation_key_expired(self):
        try:
            if now() <= self.activation_key_expires:
                return False
        except Exception as e:
            pass
        return True


class UserProfile(models.Model):
    MALE = 'M'
    FEMALE = 'F'

    Genders = (
        (MALE, 'Мужчина'),
        (FEMALE, 'Женщина')
    )

    user = models.OneToOneField(User, null=False, db_index=True, on_delete=models.CASCADE)
    about = models.TextField(verbose_name='О себе', blank=True, null=True)
    gender = models.CharField(verbose_name='пол', choices=Genders, blank=True, max_length=1)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()
