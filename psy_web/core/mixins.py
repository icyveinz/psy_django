from django.db import models
from wagtail.admin.panels import FieldPanel


class SeoMixin(models.Model):
    seo_title = models.CharField(max_length=255, blank=True, help_text="Meta title")
    seo_description = models.TextField(blank=True, help_text="Meta description")

    og_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+',
        help_text="Open Graph / Twitter image"
    )

    seo_panels = [
        FieldPanel("seo_title"),
        FieldPanel("seo_description"),
        FieldPanel("og_image"),
    ]

    class Meta:
        abstract = True