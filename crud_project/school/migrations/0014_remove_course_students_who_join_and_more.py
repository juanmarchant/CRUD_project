# Generated by Django 4.0 on 2022-02-08 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_alter_customuser_options'),
        ('school', '0013_alter_course_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='students_who_join',
        ),
        migrations.AddField(
            model_name='schoolyear',
            name='students_who_join',
            field=models.ManyToManyField(related_name='member_students', to='authentication.Student', verbose_name='Estudiantes'),
        ),
    ]
