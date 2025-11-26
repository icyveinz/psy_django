from core.models import StaticImagesPath
from wagtail_landing.models import LandingMainPage


def global_pages(request):
    return {
        "landing_page": LandingMainPage.objects.first(),
        "static_images": StaticImagesPath.objects.first(),
    }
