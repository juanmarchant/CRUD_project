from django.contrib import admin
from .models import SchoolYear
# Register your models here.


class CustomSchoolAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(SchoolYear, CustomSchoolAdmin)

