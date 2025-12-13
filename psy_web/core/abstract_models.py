from django.http import Http404
from wagtail.models import Page

# Для выброса ошибки 404 при попытке использовать папку как страницу
class AbstractFolderPage(Page):
    class Meta:
        abstract = True

    def serve(self, request, *args, **kwargs):
        raise Http404