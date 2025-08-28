from datetime import date
from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.documents.models import Document
from wagtail.fields import RichTextField
from wagtail.models import Page
from a_blog.models import BlogPage


class DocumentsFolder(Page):
    pass

# Create your models here.
class DocumentsPage(Page):
    body = RichTextField(blank=True)
    date_published = models.DateField("Post date", default=date.today)
    document = models.ForeignKey(
        Document,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    content_panels = Page.content_panels + [
        FieldPanel('body'),
        FieldPanel('document'),
        FieldPanel('date_published'),
    ]
    template = "my_docs/docs_template.html"

    def get_context(self, request, *args, **kwargs):
        from wagtail_landing.models import LandingMainPage
        context = super().get_context(request, *args, **kwargs)
        landing = LandingMainPage.objects.first()
        context['blog'] = BlogPage.objects.first()
        if landing:
            appointment_blocks = landing.appointment_blocks.all().prefetch_related(
                'social_squares', 'docs'
            )
            context['landing_page'] = LandingMainPage.objects.first()
            context['appointment_blocks'] = appointment_blocks

        return context