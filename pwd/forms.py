from django.forms import ModelForm
from .models import Generator

class GeneratorForm(ModelForm):
    class Meta:
        model = Generator
        fields = ['title', 'username', 'url', 'pwd', 'validity_date', 'sixmomth', 'twelvesmonth', 'number_digits', 'resnum', 'reschar', 'resspec']
        