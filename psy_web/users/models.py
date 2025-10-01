from datetime import date

from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.images.models import Image

# Create your models here.

class AuthorFolder(Page):
    class Meta:
        verbose_name = 'Папка для пользователей'
        verbose_name_plural = 'Папки для пользователей'
    pass

class AuthorProfile(Page):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    profile_image = models.ForeignKey(
        Image,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    bio = models.TextField(blank=True)
    date_created = models.DateField("Post date", default=date.today)

    class Meta:
        verbose_name = 'Профиль пользователя'
        verbose_name_plural = 'Профили пользователей'

    content_panels = [
        FieldPanel('title'),
        FieldPanel('name', heading='Имя пользователя'),
        FieldPanel('surname', heading='Фамилия пользователя'),
        FieldPanel('profile_image', heading='Изображения для профиля'),
        FieldPanel('bio', heading='Биография'),
        FieldPanel('date_created', heading='Когда создан'),
    ]

    def __str__(self):
        return F"AuthorProfile : {self.name} {self.surname}"