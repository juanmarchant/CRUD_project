# Generated by Django 4.0 on 2022-02-06 04:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0012_alter_course_students_who_join'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['school_year'], 'verbose_name': 'Asignatura', 'verbose_name_plural': 'Asignaturas'},
        ),
    ]
