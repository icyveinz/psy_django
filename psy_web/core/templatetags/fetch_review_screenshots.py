from django import template

from core.models import ReviewScreenshot

register = template.Library()

@register.inclusion_tag('main_landing/reviews_block/reviews_block.html', takes_context=True)
def fetch_review_screenshots(context):
    return {
        "reviews" : ReviewScreenshot.objects.all(),
    }
