from django import forms
from crudex.models import Product

class ProductForm(forms.ModelForm):
    product_value =  forms.CharField(max_length=100, help_text = "Enter Name Product")

    class Meta:
        model = Product
        fields = ('product_value',)