from django.db import models
from django.utils.translation import ugettext_lazy as _

# Create your models here.

class Client(models.Model):
    """
    =FIELDS=
    id
    name
    age
    city
    """
    #fields
    name = models.CharField(max_length=30, verbose_name="Nome do cliente")
    age = models.PositiveSmallIntegerField(verbose_name="Idade do cliente")
    city = models.CharField(max_length=30, verbose_name="Cidade do cliente")

    #Meta
    class Meta:
        verbose_name = _("Client")
        verbose_name_plural = _("Clients")
        ordering = ['-id']

    #functions
    def __str__(self):
        return self.name
