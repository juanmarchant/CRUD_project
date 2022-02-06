from django.contrib import admin
from .models import SchoolYear, Course
# Register your models here.


class CustomSchoolAdmin(admin.ModelAdmin):
    list_display = ('name','head_teacher',)

class CustomCourseAdmin(admin.ModelAdmin):
    list_display = ('name','school_year','students')

    def students(self, obj):
        return "\n".join([p.user.first_name for p in obj.students_who_join.all()])
        pass
admin.site.register(SchoolYear, CustomSchoolAdmin)
admin.site.register(Course, CustomCourseAdmin)



