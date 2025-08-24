from django.db import models

class NameBlock(models.Model):
    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    my_quote = models.CharField(max_length=250)
    title_image_href = models.CharField(max_length=200)
    hours = models.IntegerField()

    def __str__(self):
        return self.name


class EducationPiece(models.Model):
    name_block = models.ForeignKey(
        NameBlock,
        on_delete=models.CASCADE,
        related_name='education_list'
    )
    name_of_education = models.CharField(max_length=200)
    href = models.CharField(max_length=200)

    def __str__(self):
        return self.name_of_education


class ServicesBlock(models.Model):
    title = models.CharField(max_length=200)

class ServicesPiece(models.Model):
    title_block = models.ForeignKey(
        ServicesBlock,
        on_delete=models.CASCADE,
        related_name='services_list'
    )
    name_of_service = models.CharField(max_length=200)

class CertificatesBlock(models.Model):
    title = models.CharField(max_length=50)
    timing = models.CharField(max_length=50)
    online_pricing = models.CharField(max_length=30)
    actual_pricing = models.CharField(max_length=30)

class MyExperienceBlock(models.Model):
    hours_with_clients = models.CharField(max_length=200)
    hours_of_studying = models.CharField(max_length=200)
    my_quote = models.CharField(max_length=300)

class FactsPiece(models.Model):
    my_experience_block = models.ForeignKey(
        MyExperienceBlock,
        on_delete=models.CASCADE,
        related_name='facts'
    )
    fact = models.CharField(max_length=200)

class AppointmentBlock(models.Model):
    my_message = models.CharField(max_length=250)

class AppointmentSocialSquare(models.Model):
    title = models.ForeignKey(
        AppointmentBlock,
        on_delete=models.CASCADE,
        related_name='social_square'
    )
    alt_image_name = models.CharField(max_length=20)
    link_to_image = models.CharField(max_length=200)
    link_to_social = models.CharField(max_length=200)

class AppointmentDocs(models.Model):
    block = models.OneToOneField(
        AppointmentBlock,
        on_delete=models.CASCADE,
        related_name='docs'
    )
    offer = models.CharField(max_length=200)
    confidential = models.CharField(max_length=200)
    user_agreement = models.CharField(max_length=200)