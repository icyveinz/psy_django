from datetime import date
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from django.db import models


class MyWebSite(Page):
    pass

# Create your models here.
class BlogPage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    template = "a_blog/blog_page.html"
    def get_context(self, request):
        from wagtail_landing.models import LandingMainPage
        articles = self.get_children().live().order_by('-first_published_at')
        landing = LandingMainPage.objects.first()
        context = super().get_context(request)
        appointment_blocks = landing.appointment_blocks.all().prefetch_related(
            'social_squares', 'docs'
        )
        context['blog'] = BlogPage.objects.first()
        context['landing_page'] = LandingMainPage.objects.first()
        context['articles'] = articles
        context['appointment_blocks'] = appointment_blocks
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