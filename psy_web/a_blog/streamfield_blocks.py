from wagtail.blocks import (
    StreamBlock,
    RichTextBlock,
    StructBlock,
    CharBlock,
    BooleanBlock,
    URLBlock,
)
from wagtail.images.blocks import ImageChooserBlock


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
    src = URLBlock(
        required=True, help_text="Ссылка на встраиваемый контент", label="Ссылка"
    )
    allow_fullscreen = BooleanBlock(
        required=False,
        default=True,
        help_text="Разрешить fullscreen",
        label="Разрешить полноэкранный режим",
    )

    class Meta:
        icon = "site"
        label = "Вставка iframe"


class ArticleBodyBlock(StreamBlock):
    paragraph = RichTextBlock(label="Параграф")
    quote = QuoteBlock()
    custom_image = CustomImageBlock()
    iframe = IFrameBlock()

    class Meta:
        icon = "doc-full"
        label = "Содержимое статьи"
