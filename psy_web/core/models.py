from django.db import models
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel
from wagtail.models import Orderable
from wagtail.snippets.models import register_snippet


# Модель для создания повторяющегося меню снизу
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

# static_images
@register_snippet
class StaticImagesPath(Orderable):
    quotes_svg = models.CharField(max_length=200)
    top_right_arrow_svg = models.CharField(max_length=200)
    four_pointed_black_star_svg = models.CharField(max_length=200)
    certificate_image_svg = models.CharField(max_length=200)
    right_arrow_thin_svg = models.CharField(max_length=200)
    left_arrow_thin_svg = models.CharField(max_length=200)
    right_arrow_blog_entity_svg = models.CharField(max_length=200)
    pagination_left_arrow_svg = models.CharField(max_length=200)
    pagination_right_arrow_svg = models.CharField(max_length=200)
    plus_faq_svg = models.CharField(max_length=200)

    panels = [
        FieldPanel('quotes_svg'),
        FieldPanel('top_right_arrow_svg'),
        FieldPanel('four_pointed_black_star_svg'),
        FieldPanel('certificate_image_svg'),
        FieldPanel('right_arrow_thin_svg'),
        FieldPanel('left_arrow_thin_svg'),
        FieldPanel('right_arrow_blog_entity_svg'),
        FieldPanel('pagination_left_arrow_svg'),
        FieldPanel('pagination_right_arrow_svg'),
        FieldPanel('plus_faq_svg')
    ]

@register_snippet
class FAQSingleCopy(Orderable):
    faq_question = models.CharField(max_length=60)
    faq_answer = models.CharField(max_length=250)

    panels = [
        FieldPanel('faq_question'),
        FieldPanel('faq_answer'),
    ]


@register_snippet
class ReviewScreenshot(Orderable):
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE,
        related_name='+'
    )

    panels = [
        FieldPanel('image')
    ]

    def __str__(self):
        return self.image.title