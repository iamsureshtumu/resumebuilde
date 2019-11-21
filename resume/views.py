from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from resume import forms

#importing get_template from loader
from django.template.loader import get_template
 
#import render_to_pdf from util.py 
from .utils import render_to_pdf 
# Create your views here.
def resume(request):
    form=forms.ResumeForm
    return render(request,'resume.html',context={'form':form})

def display(request):
    if request.method=="POST":
        form_data=forms.ResumeForm(request.POST)
        #form is valid or not
        if form_data.is_valid():
            return render(request,'display.html',context=form_data.cleaned_data)
        else:
            return HttpResponse("INVALID FROM")
    return HttpResponse("Form Submission Error")
from django.http import HttpResponse

 
#Creating our view, it is a class based view
class GeneratePdf(View):
     def get(self, request, *args, **kwargs):
        
        #getting the template
        pdf = render_to_pdf('invoice.html')
         
         #rendering the template
        return HttpResponse(pdf, content_type='application/pdf')

    