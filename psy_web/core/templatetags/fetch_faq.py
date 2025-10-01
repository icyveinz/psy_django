from django import template

from core.models import FAQSingleCopy

register = template.Library()


@register.inclusion_tag("main_landing/faq_block/faq_block.html", takes_context=True)
def fetch_faq_blocks(context):
    return {
        "faq_blocks": FAQSingleCopy.objects.all(),
        "static_images": context.get("static_images"),
    }
