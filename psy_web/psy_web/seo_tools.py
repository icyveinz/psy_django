from django.contrib.sitemaps import Sitemap
from django.http import HttpResponse
from wagtail.models import Page


def robots_txt(request):
    content = """
User-agent: *
Disallow: /admin/
Disallow: /login/
Disallow: /cms/
Disallow: /wagtail_landing/
Allow: /

Sitemap: https://example.com/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")


class StaticPageSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Page.objects.live().public()

    def location(self, obj):
        url = obj.get_url()
        return url if url else "/"

    def lastmod(self, obj):
        return obj.latest_revision_created_at


sitemaps = {
    "pages": StaticPageSitemap,
}
