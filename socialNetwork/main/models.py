from django.db import models
from django.contrib.auth.models import AbstractUser


class AbstUser(AbstractUser):
    GENDERS = [
        ('male', 'male'),
        ('female', 'female')
    ]

    about_yourself = models.TextField(
        'о себе',
        default=' ',
        blank=False
    )

    gender = models.CharField(
        'Пол',
        choices=GENDERS,
        max_length=7,
        default='male',
        blank=False
    )
    
    class Meta(AbstractUser.Meta):
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'