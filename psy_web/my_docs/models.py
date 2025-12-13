from datetime import date
from django.db import models
from django.http import Http404
from wagtail.admin.panels import FieldPanel
from wagtail.documents.models import Document
from wagtail.fields import RichTextField
from wagtail.models import Page


class DocumentsFolder(Page):
    class Meta:
        verbose_name = "Папка для документов"
        verbose_name_plural = "Папки для документов"

    def serve(self, request, *args, **kwargs):
        raise Http404


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

    class Meta:
        verbose_name = "Экземпляр документа"
        verbose_name_plural = "Экземпляр документа"

    content_panels = Page.content_panels + [
        FieldPanel("body", heading="Документ в формате текста"),
        FieldPanel("document", heading="Выбор документа как файла"),
        FieldPanel("date_published", heading="Когда опубликован"),
    ]
    template = "my_docs/docs_template.html"
