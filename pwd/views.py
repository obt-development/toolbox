from django.views.generic import CreateView

from .models import Generator
from .forms import GeneratorForm

class GeneratorView(CreateView):
    model = Generator
    form_class = GeneratorForm
    template_name = "generator/generator.html"
    
    def generated(request):
     
        form = "Je fais mon test"#GeneratorForm(request.POST)
        return form
            
        
            
        

    