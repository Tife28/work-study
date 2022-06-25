# Generated by Django 2.2.12 on 2022-06-25 22:21

from django.db import migrations, models


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
                ('matric_no', models.CharField(max_length=35)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('level', models.CharField(choices=[('LEVEL', 'Level'), ('200', '200'), ('300', '300'), ('400', '400')], default='LEVEL', max_length=5)),
                ('dob', models.DateField()),
                ('gender', models.CharField(choices=[('GENDER', 'Gender'), ('MALE', 'Male'), ('FEMALE', 'Female')], default='GENDER', max_length=10)),
                ('faculty', models.CharField(choices=[('FACULTY', 'Faculty'), ('HUMANITIES', 'Faculty of Humanities'), ('SMS', 'Faculty of Social and Management Sciences'), ('SCIENCE', 'Faculty of Science and Science Education')], default='FACULTY', max_length=5)),
                ('department', models.CharField(max_length=300)),
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
                ('parent_approval', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No'), ('DONT_KNOW', "Don't Know")], default='DONT_KNOW', max_length=5)),
                ('library', models.BooleanField(blank=True, default=False)),
                ('cafetaria', models.BooleanField(blank=True, default=False)),
                ('supermarket', models.BooleanField(blank=True, default=False)),
                ('ict_unit', models.BooleanField(blank=True, default=False)),
                ('water_works', models.BooleanField(blank=True, default=False)),
                ('general_affairs', models.BooleanField(blank=True, default=False)),
                ('others', models.CharField(blank=True, max_length=50)),
                ('preferred', models.CharField(blank=True, max_length=50)),
                ('experience', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No'), ('DONT_KNOW', "I don't think so")], default='DONT_KNOW', max_length=20)),
                ('expdet', models.TextField(blank=True)),
                ('hrs', models.IntegerField()),
                ('declaration', models.CharField(max_length=150)),
                ('namesign', models.CharField(max_length=150)),
                ('sign', models.FileField(blank=True, upload_to='sign/')),
                ('hodrec', models.TextField(blank=True)),
                ('hodname', models.CharField(blank=True, max_length=150)),
                ('hod_date', models.DateField()),
                ('hodsign', models.FileField(blank=True, upload_to='sign/')),
                ('deanrec', models.TextField(blank=True)),
                ('deanname', models.CharField(blank=True, max_length=150)),
                ('dean_date', models.DateField()),
                ('deansign', models.FileField(blank=True, upload_to='sign/')),
                ('dsacom', models.TextField(blank=True)),
                ('dsaname', models.CharField(blank=True, max_length=150)),
                ('dsa_date', models.DateField()),
                ('dsasign', models.FileField(blank=True, upload_to='sign/')),
                ('pconsent', models.FileField(blank=True, upload_to='pconsent/')),
                ('unithead_comm', models.TextField(blank=True)),
                ('unithead_name', models.CharField(blank=True, max_length=150)),
                ('unithead_date', models.DateField()),
                ('unithead_sign', models.FileField(blank=True, upload_to='sign/')),
                ('wspcomm', models.TextField(blank=True)),
                ('wspname', models.CharField(blank=True, max_length=150)),
                ('wsp_date', models.DateField()),
                ('wspsign', models.FileField(blank=True, upload_to='sign/')),
                ('unit_posted', models.CharField(choices=[('CAFETERIA', 'Cafeteria'), ('LIBRARY', 'Library'), ('SUPERMARKET', 'Supermarket'), ('ICT UNIT', 'ICT Unit'), ('WATER WORKS', 'Water Works'), ('GENERAL AFFAIRS', 'General Affairs(Cleaning)')], max_length=8)),
                ('recomend_crit', models.CharField(choices=[('RECOMMENDED', 'Recommended for Approval'), ('NOT RECOMMENDED', 'Not Recommended')], max_length=4)),
                ('vcapprove', models.CharField(choices=[('APPROVED', 'Approved'), ('NOT APPROVED', 'Not Approved')], max_length=4)),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]