from django.contrib import admin
from .models import SchoolYear, Course
# Register your models here.


class CustomSchoolAdmin(admin.ModelAdmin):
    list_display = ('name','head_teacher')
    


class CustomCourseAdmin(admin.ModelAdmin):
    list_display = ('name','school_year','estudiantes')

    def estudiantes(self, obj):
        students = ",\n".join([p.user.first_name+ ' ' +p.user.last_name  for p in obj.students_who_join.all()])
        return students
    

admin.site.register(SchoolYear, CustomSchoolAdmin)
admin.site.register(Course, CustomCourseAdmin)



