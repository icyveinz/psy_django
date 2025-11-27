from django.shortcuts import redirect
from wagtail.models import Page

class MyWebSite(Page):
    def serve(self, request, *args, **kwargs):
        return redirect("/landings/main-landing/", permanent=False)

    class Meta:
        verbose_name = "Корень сайта"
        verbose_name_plural = "Корни сайта"