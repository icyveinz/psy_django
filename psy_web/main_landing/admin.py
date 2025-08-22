from django.contrib import admin
from .models import (
    NameBlock, EducationPiece,
    ServicesBlock, ServicesPiece,
    CertificatesBlock,
    MyExperienceBlock, FactsPiece
)

# --- NameBlock и связанные образования ---
class EducationPieceInline(admin.TabularInline):
    model = EducationPiece
    extra = 1  # сколько пустых форм показывать для добавления новых записей

@admin.register(NameBlock)
class NameBlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'my_quote', 'hours')
    inlines = [EducationPieceInline]

# --- ServicesBlock и связанные услуги ---
class ServicesPieceInline(admin.TabularInline):
    model = ServicesPiece
    extra = 1

@admin.register(ServicesBlock)
class ServicesBlockAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ServicesPieceInline]

# --- CertificatesBlock ---
@admin.register(CertificatesBlock)
class CertificatesBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'timing', 'online_pricing', 'actual_pricing')

# --- MyExperienceBlock и связанные факты ---
class FactsPieceInline(admin.TabularInline):
    model = FactsPiece
    extra = 1

@admin.register(MyExperienceBlock)
class MyExperienceBlockAdmin(admin.ModelAdmin):
    list_display = ('hours_with_clients', 'hours_of_studying', 'my_quote')
    inlines = [FactsPieceInline]