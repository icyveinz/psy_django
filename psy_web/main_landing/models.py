from django.db import models

class NameBlock(models.Model):
    name = models.CharField(max_length=25)
    my_quote = models.CharField(max_length=250)
    hours = models.IntegerField()

    def __str__(self):
        return self.name


class EducationPiece(models.Model):
    name_block = models.ForeignKey(
        NameBlock,
        on_delete=models.CASCADE,
        related_name='education_list'
    )
    name_of_education = models.CharField(max_length=120)
    href = models.CharField(max_length=120)

    def __str__(self):
        return self.name_of_education


class ServicesBlock(models.Model):
    title = models.CharField(max_length=100)

class ServicesPiece(models.Model):
    title_block = models.ForeignKey(
        ServicesBlock,
        on_delete=models.CASCADE,
        related_name='services_list'
    )
    name_of_service = models.CharField(max_length=150)

class CertificatesBlock(models.Model):
    title = models.CharField(max_length=50)
    timing = models.CharField(max_length=50)
    online_pricing = models.IntegerField()
    actual_pricing = models.IntegerField()

class MyExperienceBlock(models.Model):
    hours_with_clients = models.IntegerField()
    hours_of_studying = models.IntegerField()
    my_quote = models.CharField(max_length=250)

class FactsPiece(models.Model):
    my_expirience_block = models.ForeignKey(
        MyExperienceBlock,
        on_delete=models.CASCADE,
        related_name='facts'
    )
    fact = models.CharField(max_length=150)