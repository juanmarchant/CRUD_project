# Generated by Django 4.0 on 2022-02-03 16:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_student',
            field=models.BooleanField(default=False, help_text='Indica que este usuario es estudiante', verbose_name='Estudiante'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_teacher',
            field=models.BooleanField(default=False, help_text='Indica que este usuario es profesor', verbose_name='Profesor'),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='authentication.customuser', verbose_name='')),
            ],
        ),
    ]