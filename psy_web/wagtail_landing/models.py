from django.db import models
from modelcluster.models import ClusterableModel
from wagtail.models import Page, Orderable
from wagtail.admin.panels import FieldPanel, InlinePanel
from modelcluster.fields import ParentalKey
from a_blog.models import ArticlePage


class LandingFolder(Page):

    class Meta:
        verbose_name = "Папка для главной страницы"
        verbose_name_plural = "Папки для главной страницы"

    pass


# -------------------- LandingMainPage --------------------
class LandingMainPage(Page):
    landing_title = models.CharField(max_length=200)

    class Meta:
        verbose_name = "Главная страница"
        verbose_name_plural = "Главные страницы"

    content_panels = Page.content_panels + [
        FieldPanel("landing_title", heading="Главная страница"),
        InlinePanel("name_blocks", label="Блок обо мне"),
        InlinePanel("services_blocks", label="Блок о запросах клиента"),
        InlinePanel("certificates_blocks", label="Блок о консультациях и ценах"),
        InlinePanel("experience_blocks", label="Блок о моем опыте"),
    ]

    template = "main_landing/main_landing.html"

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["landing_title"] = self.landing_title

        # Получаем статьи так же, как в BlogPage.get_context
        articles = ArticlePage.objects.live().order_by("-first_published_at")
        context["articles"] = articles[:4]  # можно лимитировать
        return context


# -------------------- NameBlock --------------------
class NameBlock(Orderable, ClusterableModel):
    page = ParentalKey(
        LandingMainPage, on_delete=models.CASCADE, related_name="name_blocks"
    )
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    my_quote = models.CharField(max_length=250)
    title_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    hours = models.IntegerField()

    panels = [
        FieldPanel("name", heading="Имя"),
        FieldPanel("surname", heading="Фамилия"),
        FieldPanel("my_quote", heading="Моя цитата"),
        FieldPanel("title_image", heading="Изображение для профиля"),
        FieldPanel("hours", heading="Часы с клиентами"),
        InlinePanel("education_pieces", label="Блок о моем образовании"),
    ]


# -------------------- EducationPiece --------------------
class EducationPiece(Orderable):
    page = ParentalKey(NameBlock, on_delete=models.CASCADE, related_name="education_pieces")
    name_of_education = models.CharField(max_length=200)
    href = models.CharField(max_length=200)

    panels = [
        FieldPanel("name_of_education", heading="Название ВУЗ-а"),
        FieldPanel("href", heading="Ссылка на ВУЗ"),
    ]


# -------------------- ServicesBlock --------------------
class ServicesBlock(Orderable, ClusterableModel):
    page = ParentalKey(
        LandingMainPage, on_delete=models.CASCADE, related_name="services_blocks"
    )
    services_title = models.CharField(max_length=200)

    panels = [
        FieldPanel("services_title", heading="Запрос клиента"),
        InlinePanel("services_pieces", label="Решенная проблема клиента"),
    ]


class ServicesPiece(Orderable):
    services_block = ParentalKey(
        ServicesBlock, on_delete=models.CASCADE, related_name="services_pieces"
    )
    name_of_service = models.CharField(max_length=200)

    panels = [FieldPanel("name_of_service", heading="Решенная проблема клиента")]


# -------------------- CertificatesBlock --------------------
class CertificatesBlock(Orderable):
    page = ParentalKey(
        LandingMainPage, on_delete=models.CASCADE, related_name="certificates_blocks"
    )
    certificate_title = models.CharField(max_length=50)
    timing = models.CharField(max_length=50)
    online_pricing = models.CharField(max_length=30)
    actual_pricing = models.CharField(max_length=30)

    panels = [
        FieldPanel("certificate_title", heading="Название типа консультации"),
        FieldPanel("timing", heading="Время на консультацию"),
        FieldPanel("online_pricing", heading="Цена за онлайн"),
        FieldPanel("actual_pricing", heading="Цена за очную встречу"),
    ]


# -------------------- MyExperienceBlock --------------------
class MyExperienceBlock(Orderable, ClusterableModel):
    page = ParentalKey(
        LandingMainPage, on_delete=models.CASCADE, related_name="experience_blocks"
    )
    hours_with_clients = models.IntegerField()
    hours_of_studying = models.IntegerField()
    my_quote = models.CharField(max_length=300)
    profile_facts_picture = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    class Meta:
        verbose_name = "Блок о моем опыте"
        verbose_name_plural = "Блоки о моем опыте"

    panels = [
        FieldPanel("hours_with_clients", heading="Часов с клиентами"),
        FieldPanel("hours_of_studying", heading="Часов обучения"),
        FieldPanel("my_quote", heading="Моя цитата"),
        FieldPanel("profile_facts_picture", heading="Изображение для показа в фактах"),
        InlinePanel("facts_pieces", label="Факты обо мне"),
    ]


class FactsPiece(Orderable):
    page = ParentalKey(
        MyExperienceBlock, on_delete=models.CASCADE, related_name="facts_pieces"
    )
    fact = models.CharField(max_length=200)

    panels = [FieldPanel("fact", heading="Факт")]
