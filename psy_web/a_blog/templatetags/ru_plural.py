from django import template

register = template.Library()


@register.filter
def ru_minute(value):
    try:
        value = int(value)
    except (ValueError, TypeError):
        return ""
    if value % 10 == 1 and value % 100 != 11:
        return "минута"
    elif 2 <= value % 10 <= 4 and not 12 <= value % 100 <= 14:
        return "минуты"
    else:
        return "минут"
