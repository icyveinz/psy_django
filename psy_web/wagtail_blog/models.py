from wagtail.admin.panels import FieldPanel
from wagtail.models import Page
from wagtail.fields import RichTextField


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)
    content_panels = Page.content_panels + [
        FieldPanel('intro'),
    ]
    template = "wagtail_blog/blog_index_page.html"