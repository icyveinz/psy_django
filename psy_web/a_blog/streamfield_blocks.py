from wagtail.blocks import StructBlock, RichTextBlock, CharBlock, URLBlock, BooleanBlock, StreamBlock
from wagtail.images.blocks import ImageChooserBlock


class ArticleBodyBlock(StreamBlock):
    paragraph = RichTextBlock(label="Параграф")
    quote = StructBlock([
        ("text", RichTextBlock())
    ], icon="openquote", label="Цитата")
    custom_image = StructBlock([
        ("image", ImageChooserBlock()),
        ("caption", CharBlock(required=False))
    ], icon="image", label="Картинка")
    iframe = StructBlock([
        ("src", URLBlock(required=True, help_text="Ссылка на встраиваемый контент")),
        ("allow_fullscreen", BooleanBlock(required=False, default=True))
    ], icon="site", label="iFrame")


class QuoteBlock(StructBlock):
    text = RichTextBlock(label="Текст цитаты")

    class Meta:
        icon = "openquote"
        label = "Цитата"

class CustomImageBlock(StructBlock):
    image = ImageChooserBlock(label="Изображение")
    caption = CharBlock(required=False, label="Подпись")

    class Meta:
        icon = "image"
        label = "Картинка"

class IFrameBlock(StructBlock):
    src = URLBlock(required=True, help_text="Ссылка на встраиваемый контент", label="Ссылка")
    allow_fullscreen = BooleanBlock(required=False, default=True, help_text="Разрешить fullscreen", label="Разрешить полноэкранный режим")

    class Meta:
        icon = "site"
        label = "Вставка iframe"