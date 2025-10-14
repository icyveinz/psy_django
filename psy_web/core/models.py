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
        FieldPanel("my_message", heading="Обращение для клиента"),
        InlinePanel("social_squares", label="Квадрат с социальной сетью"),
        InlinePanel("docs", label="Блок для выбора документов"),
    ]

    class Meta:
        verbose_name = "Блок для записи"
        verbose_name_plural = "Блоки для записи"

    def __str__(self):
        return "Модель с информацией для отображения футера"


class AppointmentSocialSquare(Orderable):
    appointment_block = ParentalKey(
        AppointmentBlock, on_delete=models.CASCADE, related_name="social_squares"
    )
    alt_image_name = models.CharField(max_length=20)
    image = models.CharField(max_length=200)
    link_to_social = models.CharField(max_length=200)

    panels = [
        FieldPanel("alt_image_name", heading="Название картинки <alt>"),
        FieldPanel("image", heading="Выбор изображения"),
        FieldPanel("link_to_social", heading="Ссылка на социальную сеть"),
    ]


class AppointmentDocs(Orderable):
    appointment_block = ParentalKey(
        AppointmentBlock, on_delete=models.CASCADE, related_name="docs"
    )
    offer_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    confidential_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    user_agreement_page = models.ForeignKey(
        "wagtailcore.Page",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [
        PageChooserPanel("offer_page", heading="Страница с офертой"),
        PageChooserPanel(
            "confidential_page", heading="Страница с политикой конфиденциальности"
        ),
        PageChooserPanel(
            "user_agreement_page", heading="Страница с пользовательским соглашением"
        ),
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

    class Meta:
        verbose_name = "Пути для статичных картинок"
        verbose_name_plural = "Пути для статичных картинок"

    panels = [
        FieldPanel("quotes_svg"),
        FieldPanel("top_right_arrow_svg"),
        FieldPanel("four_pointed_black_star_svg"),
        FieldPanel("certificate_image_svg"),
        FieldPanel("right_arrow_thin_svg"),
        FieldPanel("left_arrow_thin_svg"),
        FieldPanel("right_arrow_blog_entity_svg"),
        FieldPanel("pagination_left_arrow_svg"),
        FieldPanel("pagination_right_arrow_svg"),
        FieldPanel("plus_faq_svg"),
    ]

    def __str__(self):
        return "Модель с путями для статичных картинок"


@register_snippet
class FAQSingleCopy(Orderable):
    faq_question = models.CharField(max_length=100)
    faq_answer = models.CharField(max_length=800)

    class Meta:
        verbose_name = "Экземпляр вопроса в FAQ"
        verbose_name_plural = "Экземпляры вопросов в FAQ"

    panels = [
        FieldPanel("faq_question", heading="Вопрос клиента"),
        FieldPanel("faq_answer", heading="Ответ для клиента"),
    ]

    def __str__(self):
        return self.faq_question


@register_snippet
class ReviewScreenshot(Orderable):
    image = models.ForeignKey(
        "wagtailimages.Image", on_delete=models.CASCADE, related_name="+"
    )

    class Meta:
        verbose_name = "Экземпляр скриншота в Отзывах"
        verbose_name_plural = "Экземпляры скриншотов в Отзывах"

    panels = [FieldPanel("image", heading="Скриншот с отзывом")]

    def __str__(self):
        return self.image.title


@register_snippet
class StudyResultsCard(Orderable, ClusterableModel):
    course_title = models.CharField(max_length=200)
    course_platform = models.CharField(max_length=200)
    year_ended = models.IntegerField()

    class Meta:
        verbose_name = "Экземпляр оконченного курса"
        verbose_name_plural = "Экземпляры оконченных курсов"

    panels = [
        FieldPanel("course_title", heading="Название курса"),
        FieldPanel("course_platform", heading="Платформа курса"),
        FieldPanel("year_ended", heading="Год окончания"),
        InlinePanel("study_results_li", label="Экземпляр полученного навыка", max_num=4),
    ]

    def __str__(self):
        return self.course_title


class StudyResultsLink(Orderable):
    page = ParentalKey(
        StudyResultsCard, on_delete=models.CASCADE, related_name="study_results_li"
    )
    skills_achieved = models.CharField(max_length=200)

    panels = [
        FieldPanel("skills_achieved", heading="Полученный навык"),
    ]
