from django.db import models

# Create your models here.

class resume(models.Model):
#General Information
    Name=models.CharField(max_length=40,)
    Email=models.EmailField(max_length=100,)
    Phno=models.CharField(max_length=10)

# Education Qualification
    Education_Degree=models.CharField(max_length=100,choices=(('Phd','phd'),('M.E/M.TECH','M.E/M.TECH'),('B.E/B.TECH','B.E/B.TECH')))
    Branch=models.CharField(max_length=100,choices=(('CSE','CSE'),('ECE','ECE'),('Civil/Mech/Others','Civil/Mech/Others')))
    Percentage=models.CharField(max_length=2)
# skill sets
    CarrerObjective=models.TextField(max_length=300)
    Areaofinterest=models.CharField(max_length=100,choices=(('IT/software','IT/software'),('BPO/KPO','BPO/KPO')))
    Technicalskills=models.TextField(max_length=300)
    Experience=models.CharField(max_length=100,choices=(('0-1 year','0-1 year'),('2-5 years','2-5 years'),('5+ years above','5+ years above')))
    Projectname=models.CharField(max_length=50)
    Projectdescription=models.TextField(max_length=1000,)
#Personal Information
    Address=models.TextField(max_length=300)
    Postalcode=models.IntegerField()
    CurrentLocation=models.CharField(max_length=20)
    DOB=models.CharField(max_length=15)
    Gender=models.CharField(max_length=10,choices=(('Male','Male'),('Female','Female')))
#Picture
    img=models.ImageField(upload_to='images/')