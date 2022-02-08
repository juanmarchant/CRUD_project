from django.contrib import admin
from .models import SchoolYear, Course
# Register your models here.


class CustomSchoolAdmin(admin.ModelAdmin):
    list_display = ('name','head_teacher')
    


class CustomCourseAdmin(admin.ModelAdmin):
    list_display = ('get_name_and_course','school_year','estudiantes')


    def get_name_and_course(self, obj):
        return obj.name + ' ' + '( ' + str(obj.school_year) + ' )'

    def estudiantes(self, obj):
        students = ",\n".join([p.user.first_name+ ' ' +p.user.last_name  for p in obj.students_who_join.all()])
        return students
    
    get_name_and_course.short_description = 'Asignatura'
    

admin.site.register(SchoolYear, CustomSchoolAdmin)
admin.site.register(Course, CustomCourseAdmin)



