from django import template
from typogrify.filters import typogrify

register = template.Library()

@register.filter
def typogrify_filter(value):
    """
    Применяет типографику к тексту.
    """
    if value:
        return typogrify(value)
    return ''
