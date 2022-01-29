from django.db import models
from localflavor.generic.models import IBANField
from django.contrib.auth.models import User


# Create your models here.

class Visitor(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    iban = IBANField(blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        verbose_name = 'visitor'

    def __str__(self):
        return self.name + ' ' + self.surname


#TODO creator control

