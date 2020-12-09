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

class Publication(models.Model):
    text = models.TextField(
        'текст',
        default = ' ',
        blank = True,
    )

    upvoted = models.IntegerField(
        'лайки',
        default= 0
    )
    
    downvoted = models.IntegerField(
        'дизлайки',
        default = 0
    )

    autor = models.ForeignKey(
        AbstUser,
        on_delete = models.CASCADE,
        verbose_name = 'автор'
    )

    titel = models.CharField(
        max_length = 15
    )

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'
    