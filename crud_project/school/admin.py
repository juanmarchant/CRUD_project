from django.contrib import admin
from .models import SchoolYear
# Register your models here.


class CustomSchoolAdmin(admin.ModelAdmin):
    list_display = ('name','head_teacher')

admin.site.register(SchoolYear, CustomSchoolAdmin)

# admin.site.register(Stude)

