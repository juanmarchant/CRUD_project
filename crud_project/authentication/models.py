from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
# Create your models here.


#  Teacher, Student
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    is_student = models.BooleanField(_('Estudiante'), default=False, help_text='Indica que este usuario es estudiante')
    is_teacher = models.BooleanField(_('Profesor'), default=False, help_text='Indica que este usuario es profesor')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']