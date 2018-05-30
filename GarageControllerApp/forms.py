from django import forms

from .models import Door_Controller

class Controller_Form(forms.ModelForm):


    class Meta:
        model = Door_Controller
        fields = ('name', 'number','street','locality','city','uniqueID','controller_type')

