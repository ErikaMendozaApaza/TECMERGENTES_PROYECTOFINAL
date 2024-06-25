from django import forms 
from service.models import *

# Formulario SEO de la página de servicio
class servicePageSEOForm(forms.ModelForm):
    class Meta:
        model = servicePageSEO
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'