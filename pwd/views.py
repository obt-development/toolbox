from xml.dom.minidom import Element
from django.shortcuts import redirect, render
from .models import Generator
from .forms import GeneratorForm

import string
import random

def generator(request):
    pwd="cahat"
    if request.method == 'POST':
        form = GeneratorForm(request.POST).save()
   
        return redirect('pwd:generator', )        
    else:
        form = GeneratorForm(request.POST)
    return render(request, 'generator/generator.html', {'form':form, 'pwd':pwd, 'generation':Generator.objects.all()})

        

    