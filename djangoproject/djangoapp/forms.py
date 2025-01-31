from django import forms
from .models import Products

class productForm(forms.Form):
    products=forms.ModelChoiceField(queryset=Products.objects.all(),label="select product: ")