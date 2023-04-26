from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from app.forms import *

def Student(request):
    SFO=StudentForm()
    d={'SFO':SFO}

    if request.method=='POST':
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            return HttpResponse(str(SFD.cleaned_data))
        else:
            return HttpResponse('data is not Valid')
    return render(request,'Student.html',d)
