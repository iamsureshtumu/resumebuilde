# Generated by Django 2.2.7 on 2019-11-22 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40)),
                ('Email', models.EmailField(max_length=100)),
                ('Phno', models.CharField(max_length=10)),
                ('Education_Degree', models.CharField(choices=[('Phd', 'phd'), ('M.E/M.TECH', 'M.E/M.TECH'), ('B.E/B.TECH', 'B.E/B.TECH')], max_length=100)),
                ('Branch', models.CharField(choices=[('CSE', 'CSE'), ('ECE', 'ECE'), ('Civil/Mech/Others', 'Civil/Mech/Others')], max_length=100)),
                ('Percentage', models.CharField(max_length=2)),
                ('CarrerObjective', models.TextField(max_length=300)),
                ('Areaofinterest', models.CharField(choices=[('IT/software', 'IT/software'), ('BPO/KPO', 'BPO/KPO')], max_length=100)),
                ('Technicalskills', models.TextField(max_length=300)),
                ('Experience', models.CharField(choices=[('0-1 year', '0-1 year'), ('2-5 years', '2-5 years'), ('5+ years above', '5+ years above')], max_length=100)),
                ('Projectname', models.CharField(max_length=50)),
                ('Projectdescription', models.TextField(max_length=1000)),
                ('Address', models.TextField(max_length=300)),
                ('Postalcode', models.IntegerField()),
                ('CurrentLocation', models.CharField(max_length=20)),
                ('DOB', models.CharField(max_length=15)),
                ('Gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('profile_pic', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Model_img',
        ),
    ]
