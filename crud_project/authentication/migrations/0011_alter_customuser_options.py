# Generated by Django 4.0 on 2022-02-08 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_alter_student_school_year'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ('last_name',)},
        ),
    ]