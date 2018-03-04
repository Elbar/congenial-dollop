from django import  forms
from .models import *


class DocumentForm(forms.ModelForm):

    class Meta:
        model = Document
        fields = '__all__'


class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        fields = '__all__'
