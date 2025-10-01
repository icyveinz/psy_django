from datetime import date
from django.core.paginator import Paginator
from django.shortcuts import redirect
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail.models import Page
from django.db import models
from a_blog.streamfield_blocks import ArticleBodyBlock
from users.models import AuthorProfile


class MyWebSite(Page):
    def serve(self, request, *args, **kwargs):
        return redirect('/landings/main-landing/', permanent=False)

    class Meta:
        verbose_name = 'Корень сайта'
        verbose_name_plural = 'Корни сайта'

# Create your models here.
class BlogPage(Page):
    template = "a_blog/blog_page.html"

    class Meta:
        verbose_name = 'Папка для статей'
        verbose_name_plural = 'Папки для статей'

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

        return context


class ArticlePage(Page):
    intro = models.CharField(max_length=80)
    body = StreamField(ArticleBodyBlock(), blank=True)
    date = models.DateField("Post date", default=date.today)
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.SET_NULL,
        null=True,
        related_name='+'
    )
    time_to_read = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = 'Статья для блога'
        verbose_name_plural = 'Статьи для блога'

    content_panels = Page.content_panels + [
        FieldPanel('intro', heading='Вступление'),
        FieldPanel('image', heading='Главное изображение'),
        FieldPanel('body', heading='Тело статьи'),
        FieldPanel('date', heading='Дата публикации'),
        FieldPanel('time_to_read', heading='Времени на прочтение'),
    ]

    def get_context(self, request, *args, **kwargs):
        from wagtail_landing.models import LandingMainPage

        context = super().get_context(request, *args, **kwargs)
        context['author'] = AuthorProfile.objects.first()

        return context
