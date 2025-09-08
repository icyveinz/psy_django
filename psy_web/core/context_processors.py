from a_blog.models import BlogPage
from core.models import StaticImagesPath
from wagtail_landing.models import LandingMainPage


def global_pages(request):
    return {
        'landing_page': LandingMainPage.objects.first(),
        'blog': BlogPage.objects.first(),
        'static_images': StaticImagesPath.objects.first()
    }
