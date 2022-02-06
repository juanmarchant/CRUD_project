from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import Student, Teacher


# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('first_name', 'last_name','email','is_staff', 'is_teacher', 'is_student')
    list_filter = ('is_superuser','is_staff', 'is_teacher','is_student')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),

        (('Informaión Personal'), {'fields': ('first_name', 'last_name', 'email')}),

        (('Permisos'), {'fields': ('is_active', 'is_staff', 'is_superuser','is_student','is_teacher','groups',)}),

        (('Datos Importantes'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Información Personal', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permisos', {
            'fields': (
                'is_superuser','is_student','is_teacher','groups'
                )
        }),
    )
    
admin.site.register(get_user_model(), CustomUserAdmin)


class GetNamesAdmin(admin.ModelAdmin):
    list_display = ['get_first_name','get_last_name','teacher_or_student']

    def get_first_name(self,obj):
        return obj.user.first_name
        
    def get_last_name(self,obj):
        return obj.user.last_name

    def teacher_or_student(self, obj):
        if obj.user.is_student:
            return obj.school_year
        
    
    get_first_name.short_description = 'Nombre'
    get_last_name.short_description = 'Apellidos'
    teacher_or_student.short_description = 'Curso'
    
admin.site.register(Student, GetNamesAdmin)
admin.site.register(Teacher, GetNamesAdmin)