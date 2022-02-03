import imp
from django.db import models
from django.utils.translation import gettext as _

from authentication.models import Teacher

# Create your models here.
class SchoolYear(models.Model):
    name = models.CharField(('Nombre'),max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    head_teacher = models.OneToOneField(Teacher,verbose_name='Profesor jefe',on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _("Año Escolar")
        verbose_name_plural = _("Años Escolares")
    
    def __str__(self):
        return self.name
    
