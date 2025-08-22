# main_landing/views.py
from django.shortcuts import render
from .models import (
    NameBlock,
    ServicesBlock,
    CertificatesBlock,
    MyExperienceBlock
)

def landing_page(request):
    name_block = NameBlock.objects.prefetch_related('education_list').first()

    services_blocks = ServicesBlock.objects.prefetch_related('services_list').all()

    certificates = CertificatesBlock.objects.all()

    experience_blocks = MyExperienceBlock.objects.prefetch_related('facts').all()

    context = {
        'name_block': name_block,
        'services_blocks': services_blocks,
        'certificates': certificates,
        'experience_blocks': experience_blocks,
    }

    return render(request, 'main_landing/main_landing.html', context)
