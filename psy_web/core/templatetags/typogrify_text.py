from django import template
from django.utils.safestring import mark_safe
from typogrify.filters import typogrify
from wagtail.rich_text import expand_db_html, RichText

register = template.Library()

@register.filter
def typogrify_filter(value):
    """
    Применяет типографику к тексту.
    """
    if value:
        return typogrify(value)
    return ''


@register.filter
def richtext_typogrify(value):
    """Применяет типографику к richtext (Wagtail)."""
    if not value:
        return ''
    # Если это объект RichText — преобразуем в строку
    if isinstance(value, RichText):
        value = str(value)
    return mark_safe(typogrify(expand_db_html(value)))