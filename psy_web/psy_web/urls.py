from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import path, include
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from psy_web.seo_tools import robots_txt, sitemaps


def trigger_error(request):
    division_by_zero = 1 / 0
urlpatterns = [
    path('admin/', admin.site.urls),
    path('cms/', include(wagtailadmin_urls)),
    path('documents/', include(wagtaildocs_urls)),
    path('wagtail_landing/', include('wagtail_landing.urls')),
    path('robots.txt', robots_txt),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('sentry-debug/', trigger_error),
    path('', include(wagtail_urls)),
]
