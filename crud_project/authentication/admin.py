from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin


# Register your models here.

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_teacher', 'is_student')

    fieldsets = (
        (None, {'fields': ('username', 'password')}),

        (('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),

        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','is_student','is_teacher','groups',)}),

        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_superuser','is_student','is_teacher','groups'
                )
        }),
    )

admin.site.register(get_user_model(), CustomUserAdmin)