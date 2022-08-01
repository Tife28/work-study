# Generated by Django 2.2.12 on 2022-08-01 15:26

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sur_name', models.CharField(max_length=150)),
                ('mid_name', models.CharField(max_length=150)),
                ('first_name', models.CharField(max_length=150)),
                ('matric_no', models.CharField(max_length=35, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('level', models.CharField(choices=[('LEVEL', 'Level'), ('200', '200'), ('300', '300'), ('400', '400')], default='LEVEL', max_length=50)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('GENDER', 'Gender'), ('MALE', 'Male'), ('FEMALE', 'Female')], default='GENDER', max_length=50)),
                ('faculty', models.CharField(blank=True, choices=[('FACULTY', 'Faculty'), ('HUMANITIES', 'Faculty of Humanities'), ('SMS', 'Faculty of Social and Management Sciences'), ('SCIENCE', 'Faculty of Science and Science Education')], default='FACULTY', max_length=50)),
                ('department', models.CharField(blank=True, max_length=300)),
                ('session', models.CharField(choices=[('SESSION', 'Session'), ('21/22', '2021/2022'), ('22/23', '2022/2023'), ('23/24', '2023/2024'), ('24/25', '2024/2025')], default='SESSION', max_length=50)),
                ('semester', models.CharField(choices=[('SEMESTER', 'Semester'), ('FIRST', '1st Semester'), ('SECOND', '2nd Semester')], default='SEMESTER', max_length=50)),
                ('cgpa', models.CharField(choices=[('CGPA', 'CGPA'), ('BELOW1', 'Below 1'), ('BETWEEN12', 'Between 1 and 2'), ('BETWEEN23', 'Between 2 and 3'), ('ABOVE3', 'Above 3')], default='CGPA', max_length=50)),
                ('reason1', models.TextField()),
                ('reason2', models.TextField(blank=True)),
                ('reason3', models.TextField(blank=True)),
                ('psur_name', models.CharField(max_length=150)),
                ('pmid_name', models.CharField(max_length=150)),
                ('pfirst_name', models.CharField(max_length=150)),
                ('occupation', models.CharField(max_length=70)),
                ('pphone', models.CharField(max_length=20)),
                ('pemail', models.EmailField(max_length=254)),
                ('parent_approval', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('DONT_KNOW', "Don't Know")], default='DONT_KNOW', max_length=50)),
                ('library', models.BooleanField(blank=True, default=False)),
                ('cafetaria', models.BooleanField(blank=True, default=False)),
                ('supermarket', models.BooleanField(blank=True, default=False)),
                ('ict_unit', models.BooleanField(blank=True, default=False)),
                ('water_works', models.BooleanField(blank=True, default=False)),
                ('general_affairs', models.BooleanField(blank=True, default=False)),
                ('others', models.CharField(blank=True, max_length=100)),
                ('preferred', models.CharField(blank=True, max_length=50)),
                ('experience', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('DONT_KNOW', "I don't think so")], default='DONT_KNOW', max_length=50)),
                ('expdet', models.TextField(blank=True)),
                ('hrs', models.IntegerField()),
                ('declaration', models.CharField(max_length=150)),
                ('namesign', models.CharField(max_length=150)),
                ('sign', models.FileField(blank=True, upload_to='sign/')),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hodrec', models.TextField()),
                ('hodname', models.CharField(max_length=150)),
                ('hod_date', models.DateField(default=datetime.date.today)),
                ('hodsign', models.FileField(blank=True, upload_to='sign/')),
                ('deanrec', models.TextField()),
                ('deanname', models.CharField(max_length=150)),
                ('dean_date', models.DateField(default=datetime.date.today)),
                ('deansign', models.FileField(blank=True, upload_to='sign/')),
                ('dsacom', models.TextField()),
                ('dsaname', models.CharField(max_length=150)),
                ('dsa_date', models.DateField(default=datetime.date.today)),
                ('dsasign', models.FileField(blank=True, upload_to='sign/')),
                ('pconsent', models.FileField(blank=True, upload_to='pconsent/')),
                ('unithead_comm', models.TextField()),
                ('unithead_name', models.CharField(max_length=150)),
                ('unithead_date', models.DateField(default=datetime.date.today)),
                ('unithead_sign', models.FileField(blank=True, upload_to='sign/')),
                ('wspcomm', models.TextField()),
                ('wspname', models.CharField(max_length=150)),
                ('wsp_date', models.DateField(default=datetime.date.today)),
                ('wspsign', models.FileField(blank=True, upload_to='sign/')),
                ('unit_posted', models.CharField(choices=[('UNIT POSTED', 'Unit Posted'), ('CAFETERIA', 'Cafeteria'), ('LIBRARY', 'Library'), ('SUPERMARKET', 'Supermarket'), ('ICT UNIT', 'ICT Unit'), ('WATER WORKS', 'Water Works'), ('GENERAL AFFAIRS', 'General Affairs(Cleaning)')], default='UNIT POSTED', max_length=150)),
                ('recomend_crit', models.CharField(choices=[('RECOMEND_CRIT', 'Recommendation Criteria'), ('RECOMMENDED', 'Recommended for Approval'), ('NOT RECOMMENDED', 'Not Recommended')], default='RECOMEND_CRIT', max_length=150)),
                ('vcapprove', models.CharField(choices=[('VCAPPROVE', 'Vice Chancellor Approval'), ('APPROVED', 'Approved'), ('NOT APPROVED', 'Not Approved')], default='VCAPPROVE', max_length=150)),
                ('student', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='wsp.Student')),
            ],
            options={
                'db_table': 'recommendation',
            },
        ),
    ]
