# Generated by Django 4.0 on 2022-02-06 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_student_school_year'),
        ('school', '0011_remove_course_student_course_students_who_join'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='students_who_join',
            field=models.ManyToManyField(related_name='member_students', to='authentication.Student', verbose_name='Estudiantes'),
        ),
    ]
