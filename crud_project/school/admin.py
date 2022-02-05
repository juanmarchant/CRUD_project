from django.contrib import admin
from .models import SchoolYear, Course
# Register your models here.


class CustomSchoolAdmin(admin.ModelAdmin):
    list_display = ('name','head_teacher',)

class CustomCourseAdmin(admin.ModelAdmin):
    pass
admin.site.register(SchoolYear, CustomSchoolAdmin)
admin.site.register(Course)



