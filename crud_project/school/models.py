from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
class SchoolYear(models.Model):
    name = models.CharField(('Nombre'),max_length=100)
    head_teacher = models.OneToOneField(to='authentication.Teacher',verbose_name='Profesor jefe',on_delete=models.CASCADE, null=True, blank=True)
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = _("Curso")
        verbose_name_plural = _("Cursos")
        ordering =['order']
    
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(('Nombre'),max_length=100)
    school_year =  models.ForeignKey(SchoolYear, verbose_name=_("Curso"), on_delete=models.CASCADE, null=True, blank=True)
    students_who_join = models.ManyToManyField(to='authentication.Student', verbose_name='Estudiantes',related_name='member_students')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = _('Asignatura')
        verbose_name_plural = _('Asignaturas')
        ordering = ['school_year']
    
    def __str__(self):
        return self.name
    
    
