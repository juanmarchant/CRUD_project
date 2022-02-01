from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext as _
# Create your models here.


#  Teacher, Student
class CustomUser(AbstractUser):
    email = models.EmailField(max_length=150, unique=True)
    is_student = models.BooleanField(_('student status'), default=False)
    is_teacher = models.BooleanField(_('teacher status'), default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','password']