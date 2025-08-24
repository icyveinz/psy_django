from django.contrib import admin
from .models import (
    NameBlock, EducationPiece,
    ServicesBlock, ServicesPiece,
    CertificatesBlock,
    MyExperienceBlock, FactsPiece, AppointmentSocialSquare, AppointmentDocs, AppointmentBlock
)

class EducationPieceInline(admin.TabularInline):
    model = EducationPiece
    extra = 1

@admin.register(NameBlock)
class NameBlockAdmin(admin.ModelAdmin):
    list_display = ('name', 'my_quote', 'hours')
    inlines = [EducationPieceInline]

class ServicesPieceInline(admin.TabularInline):
    model = ServicesPiece
    extra = 1

@admin.register(ServicesBlock)
class ServicesBlockAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [ServicesPieceInline]

@admin.register(CertificatesBlock)
class CertificatesBlockAdmin(admin.ModelAdmin):
    list_display = ('title', 'timing', 'online_pricing', 'actual_pricing')

class FactsPieceInline(admin.TabularInline):
    model = FactsPiece
    extra = 1

@admin.register(MyExperienceBlock)
class MyExperienceBlockAdmin(admin.ModelAdmin):
    list_display = ('hours_with_clients', 'hours_of_studying', 'my_quote')
    inlines = [FactsPieceInline]

class AppointmentSocialSquareInline(admin.TabularInline):
    model = AppointmentSocialSquare
    extra = 1

class AppointmentDocsInline(admin.StackedInline):
    model = AppointmentDocs
    can_delete = False
    max_num = 1

@admin.register(AppointmentBlock)
class AppointmentBlockAdmin(admin.ModelAdmin):
    list_display = ('id', 'my_message')
    inlines = [AppointmentSocialSquareInline, AppointmentDocsInline]