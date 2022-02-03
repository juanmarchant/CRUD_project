from statistics import mode
from django.db import models

# Create your models here.
class SchoolYear(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
