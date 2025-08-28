from datetime import date

from django.core.paginator import Paginator
from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from django.db import models

from users.models import AuthorProfile


class MyWebSite(Page):
    pass

# Create your models here.
class BlogPage(Page):
    body = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('body'),
    ]
    template = "a_blog/blog_page.html"

    def get_context(self, request, *args, **kwargs):
        from wagtail_landing.models import LandingMainPage

        context = super().get_context(request, *args, **kwargs)

        # --- Статьи ---
        articles = self.get_children().live().order_by('-first_published_at')

        # Пагинация: 4 статьи на страницу
        paginator = Paginator(articles, 4)
        page_number = request.GET.get('page', 1)
        page_obj = paginator.get_page(page_number)
        context['articles'] = page_obj

        # --- Главная лендинг страница ---
        landing = LandingMainPage.objects.first()
        context['landing_page'] = landing

        # --- Appointment блоки ---
        if landing:
            appointment_blocks = landing.appointment_blocks.all().prefetch_related(
                'social_squares', 'docs'
            )
            context['appointment_blocks'] = appointment_blocks

        # --- Ссылка на блог ---
        context['blog'] = BlogPage.objects.first()

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
        context['author'] = AuthorProfile.objects.first()
        if landing:
            appointment_blocks = landing.appointment_blocks.all().prefetch_related(
                'social_squares', 'docs'
            )
            context['landing_page'] = LandingMainPage.objects.first()
            context['appointment_blocks'] = appointment_blocks

        return context