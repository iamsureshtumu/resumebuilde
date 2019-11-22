from django import forms
from resume.models import resume

    
class Resume(forms.ModelForm):
    class Meta:
        model=resume
        fields='__all__'
        exclude=('img',)
    
