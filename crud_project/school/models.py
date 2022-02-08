from django.db import models

# Create your models here.
class SchoolYear(models.Model):
    name = models.CharField(('Nombre'),max_length=100)
    head_teacher = models.OneToOneField(to='authentication.Teacher',verbose_name='Profesor jefe',on_delete=models.CASCADE, null=True, blank=True)
    students_who_join = models.ManyToManyField(to='authentication.Student', verbose_name='Estudiantes',related_name='member_students')
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    class Meta:
        verbose_name = ("Curso")
        verbose_name_plural = ("Cursos")
        ordering =['order']
    
    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(('Nombre'),max_length=100)
    school_year =  models.ForeignKey(SchoolYear, verbose_name=("Curso"), on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
    class Meta:
        verbose_name = ('Asignatura')
        verbose_name_plural = ('Asignaturas')
        ordering = ['school_year']
    
    def __str__(self):
        return self.name
    
    
