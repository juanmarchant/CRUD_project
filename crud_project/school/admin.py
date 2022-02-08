from django.contrib import admin
from .models import SchoolYear, Course
# Register your models here.

# Curso - Año escolar
class CustomSchoolAdmin(admin.ModelAdmin):
    list_display = ('name','head_teacher', 'estudiantes')
    
    def estudiantes(self, obj):
        students = ",\n".join([p.user.first_name+ ' ' +p.user.last_name  for p in obj.students_who_join.all()])
        return students

# Asignaturas
class CustomCourseAdmin(admin.ModelAdmin):
    list_display = ('get_name_and_course','school_year',)


    def get_name_and_course(self, obj):
        return obj.name + ' ' + '( ' + str(obj.school_year) + ' )'


    
    get_name_and_course.short_description = 'Asignatura'
    

admin.site.register(SchoolYear, CustomSchoolAdmin)
admin.site.register(Course, CustomCourseAdmin)



