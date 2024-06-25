from django import forms 
from legal.models import *

# Formulario de términos
class termsForm(forms.ModelForm):
    class Meta:
        model = Terms
        fields = '__all__'

# Formulario de póliza
class policyForm(forms.ModelForm):
    class Meta:
        model = Policy
        fields = '__all__'