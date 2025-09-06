from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet


# Create your models here.
@register_snippet
class AppointmentBlock(Orderable, ClusterableModel):
    my_message = models.CharField(max_length=250)

    panels = [
        FieldPanel('my_message'),
        InlinePanel('social_squares', label='Social Squares'),
        InlinePanel('docs', label='Documents')
    ]

    def __str__(self):
        return self.my_message

class AppointmentSocialSquare(Orderable):
    appointment_block = ParentalKey(
        AppointmentBlock, on_delete=models.CASCADE, related_name='social_squares'
    )
    alt_image_name = models.CharField(max_length=20)
    image = models.CharField(max_length=200)
    link_to_social = models.CharField(max_length=200)

    panels = [
        FieldPanel('alt_image_name'),
        FieldPanel('image'),
        FieldPanel('link_to_social'),
    ]

class AppointmentDocs(Orderable):
    appointment_block = ParentalKey(
        AppointmentBlock, on_delete=models.CASCADE, related_name='docs'
    )
    offer_page = models.ForeignKey(
        'wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    confidential_page = models.ForeignKey(
        'wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    user_agreement_page = models.ForeignKey(
        'wagtailcore.Page', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        PageChooserPanel('offer_page'),
        PageChooserPanel('confidential_page'),
        PageChooserPanel('user_agreement_page'),
    ]