from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel, PageChooserPanel
from modelcluster.fields import ParentalKey
from a_blog.models import ArticlePage, BlogPage


class LandingFolder(Page):
    pass

# -------------------- LandingMainPage --------------------
class LandingMainPage(Page):
    landing_title = models.CharField(max_length=200)

    content_panels = Page.content_panels + [
        FieldPanel('landing_title'),
        InlinePanel('name_blocks', label='Name Blocks'),
        InlinePanel('services_blocks', label='Services Blocks'),
        InlinePanel('certificates_blocks', label='Certificates Blocks'),
        InlinePanel('experience_blocks', label='Experience Blocks'),
        InlinePanel('appointment_blocks', label='Appointment Blocks')
    ]

    template = "main_landing/main_landing.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context['landing_title'] = self.landing_title

        # Получаем статьи так же, как в BlogPage.get_context
        articles = ArticlePage.objects.live().order_by('-first_published_at')
        context['articles'] = articles[:4]  # можно лимитировать
        return context


# -------------------- NameBlock --------------------
class NameBlock(Orderable, ClusterableModel):
    page = ParentalKey(LandingMainPage, on_delete=models.CASCADE, related_name='name_blocks')
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    my_quote = models.CharField(max_length=250)
    title_image = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )
    hours = models.IntegerField()

    panels = [
        FieldPanel('name'),
        FieldPanel('surname'),
        FieldPanel('my_quote'),
        FieldPanel('title_image'),
        FieldPanel('hours'),
        InlinePanel('education_pieces', label='Education Pieces'),
    ]

# -------------------- EducationPiece --------------------
class EducationPiece(Orderable):
    page = ParentalKey(NameBlock, on_delete=models.CASCADE, related_name='education_pieces')
    name_of_education = models.CharField(max_length=200)
    href = models.CharField(max_length=200)

    panels = [
        FieldPanel('name_of_education'),
        FieldPanel('href'),
    ]

# -------------------- ServicesBlock --------------------
class ServicesBlock(Orderable, ClusterableModel):
    page = ParentalKey(LandingMainPage, on_delete=models.CASCADE, related_name='services_blocks')
    services_title = models.CharField(max_length=200)
    left_image_svg = models.CharField(max_length=200)

    panels = [
        FieldPanel('services_title'),
        FieldPanel('left_image_svg'),
        InlinePanel('services_pieces', label='Services Pieces')
    ]

class ServicesPiece(Orderable):
    services_block = ParentalKey(ServicesBlock, on_delete=models.CASCADE, related_name='services_pieces')
    name_of_service = models.CharField(max_length=200)

    panels = [FieldPanel('name_of_service')]

# -------------------- CertificatesBlock --------------------
class CertificatesBlock(Orderable):
    page = ParentalKey(LandingMainPage, on_delete=models.CASCADE, related_name='certificates_blocks')
    certificate_title = models.CharField(max_length=50)
    timing = models.CharField(max_length=50)
    online_pricing = models.CharField(max_length=30)
    actual_pricing = models.CharField(max_length=30)
    certificate_image_svg = models.CharField(max_length=200)

    panels = [
        FieldPanel('certificate_title'),
        FieldPanel('timing'),
        FieldPanel('online_pricing'),
        FieldPanel('actual_pricing'),
        FieldPanel('certificate_image_svg'),
    ]

# -------------------- MyExperienceBlock --------------------
class MyExperienceBlock(Orderable, ClusterableModel):
    page = ParentalKey(LandingMainPage, on_delete=models.CASCADE, related_name='experience_blocks')
    hours_with_clients = models.IntegerField()
    hours_of_studying = models.IntegerField()
    my_quote = models.CharField(max_length=300)
    profile_facts_picture = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True, on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('hours_with_clients'),
        FieldPanel('hours_of_studying'),
        FieldPanel('my_quote'),
        FieldPanel('profile_facts_picture'),
        InlinePanel('facts_pieces', label='Facts Pieces'),
        InlinePanel('study_results_cards', label='Study Results Cards'),
    ]

class FactsPiece(Orderable):
    page = ParentalKey(MyExperienceBlock, on_delete=models.CASCADE, related_name='facts_pieces')
    fact = models.CharField(max_length=200)

    panels = [FieldPanel('fact')]

class StudyResultsCard(Orderable, ClusterableModel):
    page = ParentalKey(MyExperienceBlock, on_delete=models.CASCADE, related_name='study_results_cards')
    course_title = models.CharField(max_length=200)
    course_platform = models.CharField(max_length=200)
    year_ended = models.IntegerField()

    panels = [
        FieldPanel('course_title'),
        FieldPanel('course_platform'),
        FieldPanel('year_ended'),
        InlinePanel('study_results_li', label='Study Results Cards', max_num=4)
    ]

class StudyResultsLink(Orderable):
    page = ParentalKey(StudyResultsCard, on_delete=models.CASCADE, related_name='study_results_li')
    skills_achieved = models.CharField(max_length=200)


# -------------------- AppointmentBlock --------------------
class AppointmentBlock(Orderable, ClusterableModel):
    page = ParentalKey(LandingMainPage, on_delete=models.CASCADE, related_name='appointment_blocks')
    my_message = models.CharField(max_length=250)

    panels = [
        FieldPanel('my_message'),
        InlinePanel('social_squares', label='Social Squares'),
        InlinePanel('docs', label='Documents')
    ]

class AppointmentSocialSquare(Orderable):
    appointment_block = ParentalKey(AppointmentBlock, on_delete=models.CASCADE, related_name='social_squares')
    alt_image_name = models.CharField(max_length=20)
    image = models.CharField(max_length=200)
    link_to_social = models.CharField(max_length=200)

    panels = [
        FieldPanel('alt_image_name'),
        FieldPanel('image'),
        FieldPanel('link_to_social'),
    ]

class AppointmentDocs(Orderable):
    appointment_block = ParentalKey(AppointmentBlock, on_delete=models.CASCADE, related_name='docs')

    offer_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    confidential_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    user_agreement_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True, blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    panels = [
        PageChooserPanel('offer_page'),
        PageChooserPanel('confidential_page'),
        PageChooserPanel('user_agreement_page'),
    ]
