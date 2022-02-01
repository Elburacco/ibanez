from django.db import models
from localflavor.generic.models import IBANField
from django.contrib.auth.models import User
from core.middleware import local

# Create your models here.

NULL_AND_BLANK = {'null': True, 'blank': True}


class BaseModel(models.Model):
    owner = models.ForeignKey(User, **NULL_AND_BLANK, on_delete=models.DO_NOTHING)

    class Meta:
        abstract = True


class Visitor(BaseModel):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    iban = IBANField(unique=True)

    class Meta:
        verbose_name = 'visitor'

    def __str__(self):
        return self.name + ' ' + self.surname

    def save(self, *args, **kwargs):
        if self.pk is None and hasattr(local, 'user'):
            self.owner = local.user
        return super(Visitor, self).save(*args, **kwargs)


#TODO creator control

