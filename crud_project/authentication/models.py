from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
from school.models import SchoolYear
# Create your models here.


#  Teacher, Student
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    is_student = models.BooleanField(_('Estudiante'), default=False, help_text='Indica que este usuario es estudiante')
    is_teacher = models.BooleanField(_('Profesor'), default=False, help_text='Indica que este usuario es profesor')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']


class Student(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    school_year = models.ForeignKey(SchoolYear, verbose_name=_("Año Escolar"),on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = _("Estudiante")
        verbose_name_plural = _("Estudiantes")
        ordering = ['school_year__order']

    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name
    

class Teacher(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Profesor")
        verbose_name_plural = _("Profesores")
        
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name    