# Generated by Django 5.0.2 on 2024-02-16 23:13

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('d_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('dept_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Elective',
            fields=[
                ('e_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('elective_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='RegistrationTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('end_time', models.TimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('s_id', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('jntu_no', models.CharField(max_length=20)),
                ('section', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('curr_sem', models.IntegerField()),
                ('department', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_portal.department')),
            ],
        ),
        migrations.CreateModel(
            name='ResultsElectiveWise',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('department', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_portal.department')),
                ('elective_name', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_portal.elective')),
                ('stu_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admin_portal.studentinfo')),
            ],
        ),
        migrations.CreateModel(
            name='ElectivesInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_code', models.CharField(max_length=20)),
                ('offering_strength', models.IntegerField()),
                ('elective_name', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_portal.elective')),
                ('offering_department', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='admin_portal.department')),
                ('not_allowed_students', models.ManyToManyField(blank=True, to='admin_portal.studentinfo')),
            ],
        ),
    ]
