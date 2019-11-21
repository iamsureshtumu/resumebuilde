from django import forms
from resume.models import Model_img

class ResumeForm(forms.Form):
#General Information
    Name=forms.CharField(min_length=4,max_length=40,required=True,label="Name")
    Email=forms.EmailField(min_length=5,max_length=100,required=True,label="Email")
    Phno=forms.CharField(required=True,max_length=10,min_length=10)

# Education Qualification
    Education=forms.ChoiceField(choices=(('Phd','phd'),('M.E/M.TECH','M.E/M.TECH'),('B.E/B.TECH','B.E/B.TECH')))
    Branch=forms.ChoiceField(choices=(('CSE','CSE'),('ECE','ECE'),('Civil/Mech/Others','Civil/Mech/Others')),widget=forms.RadioSelect)
    Percentage=forms.CharField(min_length=2,max_length=2)
# skill sets
    CarrerObjective=forms.CharField(widget=forms.Textarea,required=True)
    Areaofinterest=forms.ChoiceField(choices=(('IT/software','IT/software'),('BPO/KPO','BPO/KPO')))
    Technicalskills=forms.CharField(widget=forms.Textarea)
    Experience=forms.ChoiceField(choices=(('0-1 year','0-1 year'),('2-5 years','2-5 years'),('5+ years above','5+ years above')))
    Projectname=forms.CharField(min_length=2,max_length=50,required=False)
    Projectdescription=forms.CharField(widget=forms.Textarea)
#Personal Information
    Address=forms.CharField(widget=forms.Textarea)
    Postalcode=forms.IntegerField()
    CurrentLocation=forms.CharField(min_length=2,max_length=20)
    DOB=forms.CharField(min_length=5,max_length=15)
    Gender=forms.ChoiceField(choices=(('Male','Male'),('Female','Female')),widget=forms.RadioSelect)
#Picture
    

class from_demo(forms.ModelForm):
    class Meta:
        model=Model_img
        fields='__all__'
    
