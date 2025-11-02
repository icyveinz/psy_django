from django import template
from wagtail.rich_text import expand_db_html
from typogrify.filters import typogrify

register = template.Library()

@register.filter
def richtext_typogrify(value):
    if not value:
        return ''
    return typogrify(expand_db_html(value))