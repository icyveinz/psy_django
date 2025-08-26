from datetime import date
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from django.db import models


class HomePage(Page):
    pass

# Create your models here.
class BlogPage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    template = "a_blog/blog_page.html"
    def get_context(self, request):
        articles = self.get_children().live().order_by('-first_published_at')
        context = super().get_context(request)
        context['articles'] = articles
        return context

class ArticlePage(Page):
    intro = models.CharField(max_length=80)
    body = RichTextField(blank=True)
    date = models.DateField("Post date", default=date.today)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )
    caption = models.CharField(blank=True, max_length=80)
    time_to_read = models.PositiveIntegerField(default=0)
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
        FieldPanel('image'),
        FieldPanel('caption'),
        FieldPanel('body'),
        FieldPanel('date'),
        FieldPanel('time_to_read'),
    ]