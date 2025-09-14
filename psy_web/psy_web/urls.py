from django.contrib import admin
from django.http import HttpResponse
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls

def trigger_error(request):
    division_by_zero = 1 / 0

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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('wagtail_landing/', include('wagtail_landing.urls')),
    path('robots.txt', robots_txt),
    path('sentry-debug/', trigger_error),
    path('', include(wagtail_urls)),
]
