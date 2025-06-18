from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    expiry_date = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'type': 'date',
            }
        ),
        label="Date de péremption"
    )

    class Meta:
        model = Product
        fields = ['name', 'price', 'expiry_date']
