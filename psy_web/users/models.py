from datetime import date

from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.images.models import Image

# Create your models here.

class AuthorFolder(Page):
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

    content_panels = [
        FieldPanel('title'),
        FieldPanel('name'),
        FieldPanel('surname'),
        FieldPanel('profile_image'),
        FieldPanel('bio'),
        FieldPanel('date_created'),
    ]

    def __str__(self):
        return F"AuthorProfile : {self.name} {self.surname}"