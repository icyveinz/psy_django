from django import template

from core.models import AppointmentBlock

register = template.Library()


@register.inclusion_tag(
    "main_landing/appointment_block/appointment_block.html", takes_context=True
)
def fetch_appointment_footer(context):
    return {"appointment_block": AppointmentBlock.objects.first()}
