from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.simple_tag
def responsive_image(image, widths="400,800,1200,1600,2000", sizes="100vw", classes=""):
    """
    Генерирует <img> с srcset из Wagtail Image.
    :param image: Wagtail Image объект
    :param widths: размеры через запятую (px)
    :param sizes: атрибут sizes, по умолчанию 100vw
    :param classes: классы CSS для <img>, строка или список
    """

    if not image:
        return ""

    if isinstance(classes, (list, tuple)):
        classes = " ".join(classes)

    widths = [int(w.strip()) for w in widths.split(",")]

    srcset_parts = []
    for w in widths:
        rendition = image.get_rendition(f"width-{w}")
        srcset_parts.append(f"{rendition.url} {w}w")

    default_rendition = image.get_rendition(f"width-{widths[len(widths)//2]}")

    html = f'''
    <img 
        src="{default_rendition.url}" 
        srcset="{", ".join(srcset_parts)}" 
        sizes="{sizes}" 
        alt="{image.title}"
        loading="lazy"
        class="{classes}"
        draggable="false"
    >
    '''
    return mark_safe(html)