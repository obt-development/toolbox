from django import forms
from .models import Generator

class GeneratorForm(forms.ModelForm):
    class Meta:
        model = Generator
              
        fields = ( 'title','username', 'url', 'pwd', 'validity_date', 'caracteres', 'chiffres','lettres', 'sixmonths', 'twelvemonths' )
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control','label':'Title', 'required':True}),
            'username': forms.TextInput(attrs={'class': 'form-control' ,'label':'Your username', 'required':False}),
            'url': forms.TextInput(attrs={'class': 'form-control' ,'label':'website'}),
            'chiffres': forms.CheckboxInput(attrs={'label':'Chiffres',  'default':False}),
            'lettres': forms.CheckboxInput(attrs={'label':'Lettres', 'default':False}),
            'caracteres': forms.CheckboxInput(attrs={'label':'Caractères spéciaux', 'default':False}),
            'pwd': forms.TextInput(attrs={'class': 'form-control','label':'Mot de Passe', 'Default':False}),
            'validity_date': forms.DateInput(attrs={'label':'Date de validité', 'disabled':True}),
            'sixmonths' : forms.CheckboxInput(attrs={'label':'Caractères spéciaux', 'default':False}),
            'twelvemonths' : forms.CheckboxInput(attrs={'label':'Caractères spéciaux', 'default':False}),            
        }    
        
   